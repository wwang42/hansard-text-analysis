from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Optional

import pandas as pd
from lxml import etree


@dataclass
class HansardRecord:
    doc_id: str
    date: Optional[str]
    chamber: Optional[str]
    source_file: str
    text: str
    text_length: int
    processing_version: str = "v1.0"


def _guess_chamber_from_filename(filename: str) -> Optional[str]:
    name = filename.lower()
    if "senate" in name:
        return "Senate"
    if "house" in name or "representatives" in name or "hofreps" in name:
        return "House"
    return None


def _guess_date_from_filename(filename: str) -> Optional[str]:
    """
    Extract YYYY_MM_DD or YYYY-MM-DD from filename and convert to YYYY-MM-DD.
    e.g. Senate_2025_02_10_Official.xml -> 2025-02-10
    """
    m = re.search(r"(20\d{2})[-_](\d{2})[-_](\d{2})", filename)
    if not m:
        return None
    y, mo, d = m.group(1), m.group(2), m.group(3)
    return f"{y}-{mo}-{d}"


def _extract_text_from_xml(xml_path: Path, max_chars: int = 200_000) -> str:
    """
    Robust-ish text extraction for demo purposes.
    Goal: create a reproducible workflow exemplar, not a perfect parser.
    """
    parser = etree.XMLParser(recover=True, huge_tree=True, resolve_entities=False)
    tree = etree.parse(str(xml_path), parser)
    root = tree.getroot()

    text = " ".join(root.itertext())
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_chars:
        text = text[:max_chars] + " ..."
    return text


def load_hansard_xml_dir(xml_dir: str | Path) -> List[HansardRecord]:
    xml_dir = Path(xml_dir)
    xml_files = sorted([p for p in xml_dir.glob("*.xml") if p.is_file()])

    records: List[HansardRecord] = []
    for p in xml_files:
        chamber = _guess_chamber_from_filename(p.name)
        date = _guess_date_from_filename(p.name)
        text = _extract_text_from_xml(p)

        rec = HansardRecord(
            doc_id=p.stem,
            date=date,
            chamber=chamber,
            source_file=p.name,
            text=text,
            text_length=len(text),
        )
        records.append(rec)

    return records


def records_to_dataframe(records: List[HansardRecord]) -> pd.DataFrame:
    return pd.DataFrame([asdict(r) for r in records])


def build_hansard_sample_csv(
    xml_dir: str | Path = "data/raw",
    output_csv: str | Path = "data/processed/hansard_sample.csv",
) -> Path:
    records = load_hansard_xml_dir(xml_dir)
    df = records_to_dataframe(records)

    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    return output_csv
