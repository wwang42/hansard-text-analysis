import pandas as pd

from src.ingest import build_hansard_sample_csv
from src.metadata_model import enrich_metadata
from src.basic_analysis import top_terms, chamber_summary


def main():
    out = build_hansard_sample_csv(
        xml_dir="data/raw",
        output_csv="data/processed/hansard_sample.csv",
    )
    print(f"Generated: {out}")

    df = pd.read_csv(out)
    df = enrich_metadata(df)

    print("\n=== Preview ===")
    print(df[["doc_id", "date", "chamber", "text_length"]].head())

    print("\n=== Chamber summary ===")
    print(chamber_summary(df))

    print("\n=== Top terms (cleaned) ===")
    print(top_terms(df["text"], n=15))


if __name__ == "__main__":
    main()
