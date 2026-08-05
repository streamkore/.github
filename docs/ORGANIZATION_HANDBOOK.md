# streamkore organization handbook

> Shared operating defaults for repositories maintained under **streamkore**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

streamkore maintains core infrastructure and components for streaming, real-time media, and delivery systems. This `.github` repository is the canonical home for organization-wide community health files, reusable templates, engineering policy, and planning links.

## Repository contract

Each active repository must clearly state its purpose, ownership boundary, maturity, supported environments, local development and test commands, authoritative interfaces, release and rollback process, compatibility policy, and GitHub Project/Linear links. Media services should also document protocols and codecs, latency targets, capacity assumptions, backpressure, reconnect behavior, observability, and degraded modes.

## Change and review workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep the branch and pull request focused.
3. Explain motivation, scope, risk, validation, compatibility, migration, and rollback.
4. Test success, failure, reconnect, timeout, and resource-pressure paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless preserving commit structure materially improves auditability.

## Evidence and quality

Pull requests should include reproducible commands, environments, expected and observed results, documentation updates, and CI or local-equivalent evidence. Interface or wire-format changes require consumer impact analysis and an explicit compatibility strategy.

## Security and data

Never commit credentials, signing material, private media, production payloads, or sensitive logs. Follow `SECURITY.md` for private vulnerability reporting. Pin dependencies, actions, containers, and generated inputs where supply-chain integrity or reproducibility matters.

## Documentation and decisions

Keep examples executable, links current, assumptions explicit, and repository boundaries clear. Record architectural, protocol, compatibility, privacy, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profile, repository descriptions, topics, and READMEs are current.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Required checks reflect current reliability and security risk.
- [ ] Stale repositories are archived or explicitly marked.
- [ ] Project links resolve and completed work is reflected in GitHub and Linear.
- [ ] Shared workflows and templates are versioned, tested, and backwards compatible.
