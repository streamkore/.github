#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "product-charter.json"
with path.open(encoding="utf-8") as handle:
    charter = json.load(handle)

errors = []
def require(condition, message):
    if not condition:
        errors.append(message)

def nonempty_strings(values):
    return isinstance(values, list) and bool(values) and all(isinstance(v, str) and v.strip() for v in values)

require(charter.get("$schema") == "./product-charter.schema.json", "charter must reference the repository schema")
require(charter.get("schema_version") == 1, "schema_version must be 1")
require(charter.get("organization") == "streamkore", "organization must be streamkore")
require(charter.get("canonical_linear_project") == "github.com/streamkore", "canonical Linear project mismatch")
require(bool(re.fullmatch(r"DEN-[0-9]+", str(charter.get("decision_issue", "")))), "decision_issue must be a DEN-* identifier")
status = charter.get("status")
require(status in {"unresolved", "approved", "archived"}, "status must be unresolved, approved, or archived")
repos = charter.get("approved_repositories")
require(isinstance(repos, list) and len(repos) == len(set(repos)), "approved_repositories must be a unique list")
if isinstance(repos, list):
    require(all(isinstance(repo, str) and repo.startswith("streamkore/") for repo in repos), "approved repositories must stay inside streamkore")
require(nonempty_strings(charter.get("prohibited_assumptions")), "prohibited_assumptions must be explicit")

if status == "unresolved":
    require(repos == ["streamkore/.github"], "unresolved charter may approve only streamkore/.github")
    require(charter.get("product_definition") is None, "unresolved charter must not invent a product definition")
    for field in ("target_users", "workflows", "measurable_outcomes", "vertical_slices"):
        require(charter.get(field) == [], f"unresolved charter must keep {field} empty")
    architecture = charter.get("architecture", {})
    require(all(value is None for value in architecture.values()), "unresolved charter must not preselect architecture")
elif status == "approved":
    require(isinstance(charter.get("product_definition"), str) and charter["product_definition"].strip(), "approved charter needs a product definition")
    require(nonempty_strings(charter.get("target_users")), "approved charter needs real target users")
    require(nonempty_strings(charter.get("workflows")), "approved charter needs concrete workflows")
    require(nonempty_strings(charter.get("measurable_outcomes")), "approved charter needs measurable outcomes")
    require(isinstance(charter.get("vertical_slices"), list) and len(charter["vertical_slices"]) >= 2, "approved charter needs at least two vertical slices")
    security = charter.get("security", {})
    for field in ("data_classes", "identity_and_authorization", "trust_boundaries", "retention_and_privacy", "abuse_cases", "prohibited_uses"):
        require(nonempty_strings(security.get(field)), f"approved charter needs security.{field}")
    require(len(repos or []) >= 1, "approved charter needs an explicit minimal repository map")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)
print(f"validated {path.name}: status={status}, repositories={len(repos or [])}")
