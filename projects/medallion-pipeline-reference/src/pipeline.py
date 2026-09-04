from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable

REQUIRED_FIELDS = {"order_id", "customer_id", "status", "amount", "order_date", "updated_at"}
VALID_STATUS = {"created", "paid", "cancelled", "refunded"}


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def normalize_order(raw: dict) -> dict:
    missing = REQUIRED_FIELDS - raw.keys()
    if missing:
        raise ValueError(f"missing required fields: {sorted(missing)}")
    status = str(raw["status"]).strip().lower()
    if status not in VALID_STATUS:
        raise ValueError(f"invalid status: {status}")
    try:
        amount = Decimal(str(raw["amount"])).quantize(Decimal("0.01"))
    except InvalidOperation as exc:
        raise ValueError("amount must be numeric") from exc
    if amount < 0:
        raise ValueError("amount must be non-negative")
    order_date = datetime.fromisoformat(str(raw["order_date"])).date().isoformat()
    updated_at = parse_iso(str(raw["updated_at"])).isoformat()
    return {
        "order_id": str(raw["order_id"]).strip(),
        "customer_id": str(raw["customer_id"]).strip(),
        "status": status,
        "amount": str(amount),
        "order_date": order_date,
        "updated_at": updated_at,
    }


def deduplicate_latest(records: Iterable[dict]) -> list[dict]:
    latest = {}
    for record in records:
        current = latest.get(record["order_id"])
        if current is None or parse_iso(record["updated_at"]) > parse_iso(current["updated_at"]):
            latest[record["order_id"]] = record
    return sorted(latest.values(), key=lambda row: row["order_id"])


def build_daily_revenue(records: Iterable[dict]) -> list[dict]:
    revenue = defaultdict(lambda: Decimal("0.00"))
    paid_orders = defaultdict(int)
    for record in records:
        if record["status"] == "paid":
            day = record["order_date"]
            revenue[day] += Decimal(record["amount"])
            paid_orders[day] += 1
    return [
        {"order_date": day, "paid_orders": paid_orders[day], "revenue": str(revenue[day].quantize(Decimal("0.01")))}
        for day in sorted(revenue)
    ]


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at line {line_number}") from exc
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def run(input_path: Path, output_dir: Path) -> None:
    bronze = read_jsonl(input_path)
    silver = deduplicate_latest(normalize_order(row) for row in bronze)
    gold = build_daily_revenue(silver)
    write_csv(
        output_dir / "bronze_orders.csv",
        [{key: row.get(key, "") for key in sorted(REQUIRED_FIELDS)} for row in bronze],
        sorted(REQUIRED_FIELDS),
    )
    write_csv(
        output_dir / "silver_orders.csv",
        silver,
        ["order_id", "customer_id", "status", "amount", "order_date", "updated_at"],
    )
    write_csv(
        output_dir / "gold_daily_revenue.csv",
        gold,
        ["order_date", "paid_orders", "revenue"],
    )
    print(f"bronze={len(bronze)} silver={len(silver)} gold={len(gold)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.input, args.output)


if __name__ == "__main__":
    main()
