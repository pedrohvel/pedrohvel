<div align="center">

# Harrison Grant Vail

### Data Engineer · Lakehouse · Distributed Systems · Cloud Data Platforms

Building reliable, governed and scalable data platforms with **Python, SQL, PySpark, Databricks and dbt**.

[![GitHub](https://img.shields.io/badge/GitHub-harrisvailvelame-181717?style=flat-square&logo=github)](https://github.com/harrisvailvelame)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harrison%20Grant%20Vail-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/harrison-grant-vail)
![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-0A66C2?style=flat-square)
![Cloud](https://img.shields.io/badge/Cloud-Azure%20%7C%20GCP%20%7C%20AWS-555?style=flat-square)

</div>

---

## About

Data Engineer focused on designing and implementing data platforms across the full lifecycle: **ingestion, transformation, modeling, orchestration, governance, quality and analytical serving**.

My recent engineering work is centered on **lakehouse architectures**, distributed processing and cloud data ecosystems. I prefer systems that are explicit about contracts, observable in production, safe to rerun and easy for other engineers to understand.

```text
Source systems
    ↓
Ingestion / CDC
    ↓
Bronze / Landing
    ↓
Quality + normalization
    ↓
Silver / trusted models
    ↓
Business transformations
    ↓
Gold / marts / serving
    ↓
BI · APIs · Analytics · ML
```

## Core stack

<table>
<tr>
<td valign="top" width="50%">

### Data Engineering
- Python
- SQL
- PySpark
- Apache Spark
- dbt
- Apache Airflow
- Kafka
- NiFi

### Lakehouse & Storage
- Databricks
- Delta Lake
- Apache Iceberg
- Nessie
- MinIO
- ADLS Gen2
- Amazon S3
- Google Cloud Storage

</td>
<td valign="top" width="50%">

### Cloud
- Microsoft Azure
- Google Cloud Platform
- Amazon Web Services

### Platform & Governance
- Unity Catalog
- Data quality
- Data lineage
- RLS / access controls
- Terraform
- Docker
- Git / CI/CD
- Linux

</td>
</tr>
</table>

## Selected engineering work

### 01 · Medallion Pipeline Reference
**Bronze → Silver → Gold reference pipeline**

Runnable reference implementation with schema validation, deterministic deduplication, data-quality rules, idempotent outputs and business-level aggregation.

[Open project →](./projects/medallion-pipeline-reference)

`Python` · `Data Quality` · `Medallion` · `Testing`

### 02 · dbt Quality Mart
**Analytics engineering with explicit model quality**

Staging and mart layers with dbt tests, documented grain and reusable transformation conventions.

[Open project →](./projects/dbt-quality-mart)

`dbt` · `SQL` · `Testing` · `Dimensional Modeling`

### 03 · Business Intelligence Dashboards
Power BI portfolio focused on business analysis and decision support.

[Open repository →](https://github.com/harrisvailvelame/Dashboards)

### 04 · Earlier ML work
Earlier data-science projects remain available as supporting evidence, while the primary portfolio focus is now Data Engineering.

[Browse repositories →](https://github.com/harrisvailvelame?tab=repositories)

---

## Architecture principles

**Contracts before pipelines**  
Schemas, ownership, grain and quality expectations should be explicit and testable.

**Idempotency by design**  
A production pipeline should be safe to rerun without corrupting state or duplicating business facts.

**Separate technical and business layers**  
Raw ingestion, trusted transformation and analytical serving have different responsibilities and change cycles.

**Observe data, not only jobs**  
A successful scheduler run does not prove that the resulting data is correct.

**Optimize from evidence**  
Partitioning, file sizing, caching and compute strategy should follow measured bottlenecks.

---

## Education

- **Postgraduate Specialization — Data Architecture & Strategy**, PUC Minas
- **Postgraduate Specialization — Data Engineering**, Anhanguera
- **Technology Degree — Data Science**, Unicesumar

---

## Current technical interests

`Lakehouse Architecture` · `Databricks` · `Delta Lake` · `Apache Iceberg` · `PySpark` · `dbt` · `Data Quality` · `Governance` · `Distributed Processing` · `Cloud Data Platforms`

---

<div align="center">

**Engineering portfolio based on public or synthetic data. No employer/client proprietary code is published here.**

</div>
