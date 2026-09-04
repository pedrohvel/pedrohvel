<div align="center">

# Harrison Grant Vail

### Data Engineer · Lakehouse Architecture · Distributed Data Systems

I build **reliable, governed and scalable data platforms** from ingestion and transformation through trusted analytical serving.

[![Portfolio CI](https://github.com/harrisvailvelame/pedrohvel/actions/workflows/ci.yml/badge.svg)](https://github.com/harrisvailvelame/pedrohvel/actions/workflows/ci.yml)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harrison%20Grant%20Vail-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/harrison-grant-vail)
[![GitHub](https://img.shields.io/badge/GitHub-harrisvailvelame-181717?style=flat-square&logo=github)](https://github.com/harrisvailvelame)
![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-555?style=flat-square)

</div>

---

## What I build

My work spans the full data-platform lifecycle:

```text
Operational / external sources
            ↓
      Ingestion · CDC
            ↓
      Bronze / Landing
            ↓
Contracts · Quality · Normalization
            ↓
      Silver / Trusted
            ↓
 Business transformations
            ↓
       Gold / Marts
            ↓
 BI · APIs · Analytics · ML
```

I optimize for systems that are **safe to rerun, explicit about data contracts, observable, governable and understandable by the next engineer**.

## Engineering experience

### Azure lakehouse
Production-oriented patterns using **Azure Databricks, Delta Lake, Unity Catalog, ADLS Gen2 and Azure Data Factory**, including Medallion layers, incremental data movement and governed analytical serving.

### Open lakehouse & distributed SQL
Data-platform patterns with **Apache Spark, Apache Iceberg, Nessie, MinIO, Trino and dbt**, emphasizing separation between storage, catalog, compute and transformation layers.

### Google Cloud data pipelines
Data-processing experience with **BigQuery, Dataflow and Cloud Storage**, including analytical data preparation and cloud-native processing workflows.

### Analytics serving
Power BI experience covering **semantic modeling, KPI design, Power Query, DAX, RLS and decision-oriented dashboards**.

---

## Featured engineering portfolio

| Project | What it demonstrates | Stack |
|---|---|---|
| **[Medallion Pipeline Reference](./projects/medallion-pipeline-reference)** | Bronze → Silver → Gold processing, validation, deterministic deduplication, idempotent output and tested business aggregation | Python · Testing · Data Quality |
| **[dbt Quality Mart](./projects/dbt-quality-mart)** | Staging/mart separation, model grain, reusable SQL conventions and explicit dbt quality tests | dbt · SQL · Dimensional Modeling |
| **[Asset Ingestion Pipeline](https://github.com/harrisvailvelame/images_db)** | File ingestion, media routing, image optimization, tokenization, safe Git automation and CI | Python · Pillow · Bash · GitHub Actions |
| **[Business Intelligence Dashboards](https://github.com/harrisvailvelame/Dashboards)** | Analytical serving, KPI design and Power BI report iteration | Power BI · DAX · Power Query |

### CI-backed reference implementations

The engineering examples in this repository use **public or synthetic data** and include automated checks. The portfolio CI validates the Medallion reference pipeline on every push.

---

## Earlier Data Science work

These repositories are retained as historical evidence of my progression from Data Science into Data Engineering. Their READMEs now document scope and reproducibility without presenting experimental results as production benchmarks.

| Project | Focus |
|---|---|
| [Fashion MNIST CNN](https://github.com/harrisvailvelame/Fashion_MNIST_project_using_convolucional_neural_networks) | CNN image classification with Keras |
| [Diabetes Risk Classification](https://github.com/harrisvailvelame/Forecast_diabetes) | Structured-data binary classification |
| [Red Wine Quality Modeling](https://github.com/harrisvailvelame/Forecast_vinho_do_porto) | Regression-oriented exploratory modeling |
| [Car Price Regression](https://github.com/harrisvailvelame/Previsao_preco_carros) | Regression and cross-validation |

---

## Core stack

| Domain | Technologies |
|---|---|
| **Languages** | Python · SQL · PySpark |
| **Processing** | Apache Spark · Trino · Kafka / PubSub |
| **Transformation & orchestration** | dbt · Airflow · NiFi · Pentaho |
| **Lakehouse** | Databricks · Delta Lake · Apache Iceberg · Nessie · MinIO |
| **Azure** | ADLS Gen2 · ADF · Unity Catalog |
| **GCP** | BigQuery · Dataflow · Cloud Storage |
| **AWS** | S3 · Glue · Redshift · EMR · Athena |
| **Platform** | Docker · Terraform · Git · Linux · CI/CD |
| **Governance & quality** | Catalog · Lineage · Data Quality · RLS · LGPD-oriented controls |
| **Analytics** | Power BI · DAX · Power Query |

---

## Engineering principles

**Contracts before pipelines**  
Schema, grain, ownership and quality expectations should be explicit and testable.

**Idempotency by design**  
Reprocessing should not duplicate business facts or corrupt state.

**Separate technical and business layers**  
Landing, trusted transformation and analytical serving have different responsibilities and change cycles.

**Observe data, not only jobs**  
A green scheduler does not prove that the resulting data is correct.

**Optimize from evidence**  
Partitioning, file sizing, caching and compute strategy should follow measured bottlenecks.

**Prefer boring reliability over accidental complexity**  
A clear system that can be operated safely is more valuable than an impressive diagram nobody can maintain.

---

## Education

- **Postgraduate Specialization — Data Architecture & Strategy**, PUC Minas
- **Postgraduate Specialization — Data Engineering**, Anhanguera
- **Technology Degree — Data Science**, Unicesumar

## Current interests

`Lakehouse Architecture` · `Databricks` · `Delta Lake` · `Apache Iceberg` · `PySpark` · `dbt` · `Data Quality` · `Governance` · `Distributed Processing` · `Cloud Data Platforms`

## Contact

- [LinkedIn — Harrison Grant Vail](https://www.linkedin.com/in/harrison-grant-vail)
- [GitHub — @harrisvailvelame](https://github.com/harrisvailvelame)

---

<div align="center">

**Public portfolio only. No employer or client proprietary code/data is published here.**

</div>
