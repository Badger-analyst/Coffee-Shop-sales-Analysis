"""
Data Generator — Coffee Shop Sales
====================================
Generates a realistic synthetic sales dataset for Jan–Mar 2023.

Run this FIRST before analysis.py:
    python generate_data.py

Output: data/sales_data.csv

Note: random.seed(42) is set so results are fully reproducible —
      every run will produce identical data and identical chart outputs.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import random
import os

# ── Reproducibility ───────────────────────────────────────────────────────────
random.seed(42)
np.random.seed(42)

# ── Config ────────────────────────────────────────────────────────────────────
START_DATE = datetime(2023, 1, 1)
END_DATE   = datetime(2023, 3, 31)
date_range = pd.date_range(start=START_DATE, end=END_DATE)

ITEMS = {
    # item_name: (min_price, max_price)
    "Espresso":   (2.00, 5.00),
    "Americano":  (2.00, 5.00),
    "Tea":        (2.00, 5.00),
    "Latte":      (3.00, 6.00),
    "Cappuccino": (3.00, 6.00),
    "Mocha":      (3.00, 6.00),
    "Pastry":     (1.50, 4.00),
    "Sandwich":   (1.50, 4.00),
    "Cake":       (1.50, 4.00),
    "Cookie":     (1.50, 4.00),
}

# ── Generate Transactions ─────────────────────────────────────────────────────
os.makedirs("data", exist_ok=True)

data = []
for date in date_range:
    num_transactions = random.randint(20, 100)
    for _ in range(num_transactions):
        item = random.choice(list(ITEMS.keys()))
        min_p, max_p = ITEMS[item]
        quantity = random.randint(1, 5)
        price    = round(random.uniform(min_p, max_p), 2)
        total    = round(quantity * price, 2)
        data.append([date.strftime("%Y-%m-%d"), item, quantity, price, total])

# ── Save ──────────────────────────────────────────────────────────────────────
df = pd.DataFrame(data, columns=["Date", "Item", "Quantity", "Price", "Total"])
df.to_csv("data/sales_data.csv", index=False)

print(f"✓ Dataset generated: data/sales_data.csv")
print(f"  Rows      : {len(df):,}")
print(f"  Date range: {df['Date'].min()} → {df['Date'].max()}")
print(f"  Items     : {df['Item'].nunique()} unique products")
print(f"  Est. Total Revenue: ${df['Total'].sum():,.2f}")
print("\n  Next step: python analysis.py")
