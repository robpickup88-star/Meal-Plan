#!/usr/bin/env python3
"""Turn an Infinity Foods price list CSV into a compact file for the Claude Project.

Usage:
    python3 tools/slim_price_list.py price-lists/sept_and_oct_2026.csv

Writes infinity-foods-prices.csv next to the README. It keeps only the columns
Claude needs, drops admin rows ("PLEASE PHONE ...") and barcodes, and adds a
price per kg or litre so pack sizes can be compared.
"""

import csv
import re
import sys
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "infinity-foods-prices.csv"

# Convert to kg or litres.
UNIT_FACTORS = {"g": ("kg", 0.001), "kg": ("kg", 1), "ml": ("l", 0.001), "l": ("l", 1)}

FIELDS = [
    "code",
    "description",
    "brand",
    "organic",
    "case",
    "case_price",
    "vat",
    "price_per",
    "rrp_each",
]


def case_quantity(row):
    """Total kg or litres in a case, or None for counted items."""
    unit = row["unit"].strip().lower()
    if unit not in UNIT_FACTORS:
        return None
    try:
        units = float(row["units case"] or 1)
        # Multipacks have a pack size like "4x400".
        pack = 1.0
        for part in row["pk size"].lower().split("x"):
            pack *= float(part)
    except ValueError:
        return None
    base_unit, factor = UNIT_FACTORS[unit]
    return units * pack * factor, base_unit


def slim(row):
    try:
        case_price = float(row["Case price"])
    except ValueError:
        return None
    if case_price <= 0:
        return None

    price_per = ""
    qty = case_quantity(row)
    if qty and qty[0] > 0:
        price_per = f"{case_price / qty[0]:.2f}/{qty[1]}"

    # Spice descriptions carry a batch date like "[280828]".
    description = re.sub(r"\s*\[\d+\]\s*$", "", row["product description"]).strip()

    return {
        "code": row["Product code"].strip(),
        "description": description,
        "brand": row["brand"].strip(),
        "organic": row["organic"].strip().lower(),
        "case": row["concatprodsize as text"].strip(),
        "case_price": f"{case_price:.2f}",
        "vat": "20%" if row["Vat Marker"].strip() == "V" else "0%",
        "price_per": price_per,
        "rrp_each": row["RRP rounded to 2"].strip(),
    }


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    with source.open(encoding="utf-8-sig", newline="") as f:
        rows = [r for r in map(slim, csv.DictReader(f)) if r]

    with OUTPUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} products to {OUTPUT.name} (from {source.name})")


if __name__ == "__main__":
    main()
