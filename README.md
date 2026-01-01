# Hansard Text Analysis Demo

This project demonstrates an end-to-end, reproducible text analysis workflow using  Australian Parliamentary Hansard transcripts.

The goal is to illustrate how structured metadata, basic NLP techniques, and exploratory analysis can be combined to study institutional speech patterns in a research-oriented data pipeline.

---

## Motivation

Parliamentary debates provide a rich source of longitudinal text data. This demo explores whether basic speech characteristics differ between the House of Representatives and the Senate, using a small, controlled sample.

The focus is not on advanced NLP models, but on clarity, reproducibility, and analytical reasoning.

---

## Data

- Source: Australian Parliamentary Hansard (official XML transcripts)
- Scope: Four sitting days for each chamber (House and Senate)
- Processing version: `v1.0`

Raw XML files are parsed and converted into a normalized CSV format prior to analysis.

---

## Processing Pipeline

1. XML ingestion and text extraction
2. Metadata normalization (date, chamber, document ID)
3. Text enrichment:
   - word counts
   - character counts
4. Versioned processed dataset (`data/processed/hansard_sample.csv`)

Project root discovery is handled programmatically to ensure the notebook can be run from different locations.

---

## Analysis

The analysis focuses on three descriptive dimensions:

- Total and average word counts per sitting day
- Comparison of speech volume between chambers
- High-frequency term exploration

All analysis steps are implemented using modular Python functions under `src/`.

---

## Key Findings (Sample-Level)

- Senate sittings contain slightly more spoken words per day than House sittings in this sample.
- High-frequency terms reflect institutional language (e.g. *government*, *minister*, *bill*), indicating clean text extraction.

These findings are descriptive and sample-limited, and are not intended as general conclusions.

---

## Limitations and Future Work

- The sample size is small and not temporally representative.
- Speaker-level or party-level analysis is not included.
- Future extensions could include:
  - TF-IDF–based keyword comparisons between chambers
  - Longitudinal analysis across multiple parliamentary sessions
  - Speaker attribution and role-based language analysis


## Data source and licence

This project uses publicly available Australian Hansard transcripts for demonstration purposes.

Source: Australian Parliament Hansard (XML format)  
Licence: CC-BY-NC-ND  
The data are used here solely for non-commercial, research and workflow demonstration purposes.
