import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from pipeline import build_daily_revenue, deduplicate_latest, normalize_order


class PipelineTests(unittest.TestCase):
    def test_normalize_order(self):
        row = normalize_order({
            "order_id": 1,
            "customer_id": "c1",
            "status": " PAID ",
            "amount": "10.5",
            "order_date": "2026-09-01",
            "updated_at": "2026-09-01T12:00:00Z",
        })
        self.assertEqual(row["status"], "paid")
        self.assertEqual(row["amount"], "10.50")

    def test_deduplicate_latest(self):
        rows = [
            {"order_id": "1", "updated_at": "2026-09-01T10:00:00+00:00"},
            {"order_id": "1", "updated_at": "2026-09-01T11:00:00+00:00"},
        ]
        result = deduplicate_latest(rows)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["updated_at"], "2026-09-01T11:00:00+00:00")

    def test_daily_revenue_uses_paid_only(self):
        rows = [
            {"status": "paid", "order_date": "2026-09-01", "amount": "10.00"},
            {"status": "cancelled", "order_date": "2026-09-01", "amount": "99.00"},
            {"status": "paid", "order_date": "2026-09-01", "amount": "2.50"},
        ]
        result = build_daily_revenue(rows)
        self.assertEqual(result[0]["paid_orders"], 2)
        self.assertEqual(result[0]["revenue"], "12.50")


if __name__ == "__main__":
    unittest.main()
