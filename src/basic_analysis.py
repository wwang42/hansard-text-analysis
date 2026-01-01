from __future__ import annotations

from collections import Counter
from typing import Iterable, Tuple

import pandas as pd

from .clean_text import tokenize


def top_terms(text_series: pd.Series, n: int = 20) -> list[tuple[str, int]]:
    counter = Counter()
    for t in text_series.fillna("").astype(str):
        counter.update(tokenize(t))
    return counter.most_common(n)


def chamber_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic per-chamber summary stats.
    """
    if "chamber" not in df.columns:
        df = df.assign(chamber="Unknown")

    summary = (
        df.groupby("chamber", dropna=False)
        .agg(
            docs=("doc_id", "count") if "doc_id" in df.columns else ("chamber", "count"),
            total_words=("n_words", "sum") if "n_words" in df.columns else ("chamber", "count"),
            avg_words=("n_words", "mean") if "n_words" in df.columns else ("chamber", "count"),
        )
        .reset_index()
    )
    return summary
