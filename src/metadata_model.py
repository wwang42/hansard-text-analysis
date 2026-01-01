from __future__ import annotations

from datetime import datetime
from typing import Optional

import pandas as pd


def _safe_parse_date(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    try:
        # expects YYYY-MM-DD
        datetime.strptime(s, "%Y-%m-%d")
        return s
    except Exception:
        return None


def enrich_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add basic, research-friendly metadata fields.
    """
    out = df.copy()

    # Ensure expected columns exist
    for col in ["date", "chamber", "source_file", "text"]:
        if col not in out.columns:
            out[col] = None

    out["date"] = out["date"].apply(_safe_parse_date)

    # Fill unknown chamber as "Unknown"
    out["chamber"] = out["chamber"].fillna("Unknown")

    # Basic text stats
    out["n_chars"] = out["text"].fillna("").astype(str).apply(len)
    out["n_words"] = out["text"].fillna("").astype(str).apply(lambda x: len(x.split()))

    return out
