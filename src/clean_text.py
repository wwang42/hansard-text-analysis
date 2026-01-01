from __future__ import annotations

import re

# A tiny stopword list for demo purposes (keep it small & transparent)
STOPWORDS = {
    "the", "and", "to", "of", "in", "a", "is", "for", "on", "that", "with", "as",
    "are", "be", "this", "it", "by", "or", "from", "at", "an", "was", "we", "i",
}


def clean_text(text: str) -> str:
    """
    Minimal, transparent cleaning suitable for an exemplar workflow demo.
    """
    if not isinstance(text, str):
        return ""

    # Lowercase
    t = text.lower()

    # Remove URLs
    t = re.sub(r"https?://\S+|www\.\S+", " ", t)

    # Keep letters/numbers and spaces
    t = re.sub(r"[^a-z0-9\s]", " ", t)

    # Collapse whitespace
    t = re.sub(r"\s+", " ", t).strip()

    return t


def tokenize(text: str) -> list[str]:
    """
    Simple whitespace tokenization + stopword filtering.
    """
    t = clean_text(text)
    tokens = [w for w in t.split(" ") if w and w not in STOPWORDS and len(w) > 2]
    return tokens
