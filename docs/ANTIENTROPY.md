# GitHub Antientropy Policy

This document defines the maintenance rules for Harrison Grant Vail's GitHub repositories.

The objective is to keep every repository in one explicit state: **core, supporting, historical, incubating, operational or archived**. No repository should remain ambiguous.

## Repository map

### Core public engineering

| Repository | Role |
|---|---|
| `pedrohvel` | Primary Data Engineering portfolio and reference implementations |
| `images_db` | Asset-ingestion / media-processing automation with CI |

### Supporting public work

| Repository | Role |
|---|---|
| `Dashboards` | Power BI analytical-serving portfolio |

### Historical public Data Science

| Repository | Role |
|---|---|
| `Fashion_MNIST_project_using_convolucional_neural_networks` | Historical CNN image-classification work |
| `Forecast_diabetes` | Historical tabular binary-classification work |
| `Forecast_vinho_do_porto` | Historical red-wine quality modeling |
| `Previsao_preco_carros` | Historical regression work |

Historical repositories remain available as evidence of technical progression, but they should not compete with the current Data Engineering positioning.

### Private operational repositories

| Repository | Role |
|---|---|
| `projetos` | Incubator for experiments and automation before promotion |
| `DB_JOBS` | Job-search data-layer boundary |
| `antientropia-obsidian` | Private knowledge and operating-system workspace |

## Non-negotiable repository rules

Every active repository should have:

1. a clear README;
2. an explicit purpose;
3. stable, descriptive filenames;
4. no machine-specific absolute paths;
5. no credentials, session data or secrets;
6. generated/cache files ignored by default;
7. reproducibility instructions when code is intended to run;
8. automated validation when practical;
9. public/private boundaries appropriate to the data;
10. a clear relationship to the current portfolio narrative.

## Naming

Prefer:

```text
snake_case.py
clear_project_name.ipynb
stable_artifact_name.pdf
stable_artifact_name.pbix
```

Avoid:

- personal-name suffixes in project files;
- temporary names such as `final2`, `teste`, `novo`, `Inserir um título`;
- unexplained initials;
- machine/user-specific paths;
- generic commit messages such as `up`, `update` and `fix` without context.

## Promotion path

```text
Idea
 ↓
Private incubator (`projetos`)
 ↓
Clear problem + reproducible execution
 ↓
Tests / validation + README
 ↓
Dedicated repository
 ↓
Public portfolio only if the project strengthens current positioning
```

A project does **not** become public merely because it works. It should improve the signal-to-noise ratio of the profile.

## Public portfolio hierarchy

Recruiter-facing order:

1. current Data Engineering reference work;
2. operational automation / platform tooling;
3. analytics serving / BI;
4. historical Data Science as supporting evidence.

## Weekly antientropy check

- [ ] Any repo without a README?
- [ ] Any unclear or generic filename introduced?
- [ ] Any hardcoded local path?
- [ ] Any generated database/cache/log accidentally tracked?
- [ ] Any secret or credential risk?
- [ ] Any CI failure?
- [ ] Any project that should be promoted out of the incubator?
- [ ] Any public project that no longer strengthens the portfolio?
- [ ] Any duplicated documentation or obsolete link?
- [ ] Any open loop without a next action?

## Manual structural backlog

These items require repository/account administration rather than normal content writes:

- create or rename the GitHub profile repository to exactly `harrisvailvelame/harrisvailvelame` so the portfolio README appears directly on the profile homepage;
- rename legacy repository names where appropriate while preserving redirects;
- curate pinned repositories so current Data Engineering work appears before historical ML work;
- normalize repository descriptions/topics in GitHub metadata.

Until those administrative changes are available through the integration, repository contents should remain clean and internally consistent.
