# ☕ Coffee Shop Sales Analysis

> A Python-based exploratory data analysis (EDA) of **3 months of coffee shop transactional data (Jan–Mar 2023)**.  
> Demonstrates end-to-end data skills: data generation, cleaning, aggregation, visualisation, and business insight generation.

---

## 📊 Visualisations

| Monthly Sales | Top Items by Revenue | Daily Trend |
|:---:|:---:|:---:|
| ![Monthly Sales](images/monthly_sales.png) | ![Top Items](images/top_items_revenue.png) | ![Daily Trend](images/daily_sales_trend.png) |

---

## 🎯 Project Objectives

This project answers four real business questions a coffee shop owner would ask:

1. **How much revenue did we make — and how is it trending month to month?**
2. **Which products drive the most revenue vs. the most volume?**
3. **When are our busiest and slowest days, and why?**
4. **Where should we focus inventory, staffing, and promotions?**

---

## 📁 Repository Structure

```
Coffee-Shop-sales-Analysis/
│
├── README.md                    ← Project overview, findings, and how to run
├── generate_data.py             ← Synthetic data generator (reproducible)
├── analysis.py                  ← Main EDA script — run this for all outputs
│
├── data/
│   └── sales_data.csv           ← Generated dataset (~5,000–9,000 transactions)
│
├── images/
│   ├── monthly_sales.png        ← Bar chart: revenue by month
│   ├── top_items_revenue.png    ← Pie chart: top 5 items by revenue
│   └── daily_sales_trend.png   ← Line chart: daily revenue Jan–Mar
│
└── docs/
    ├── data-dictionary.md       ← Column definitions and data types
    └── insights.md              ← Full business findings writeup
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| pandas | Data loading, cleaning, groupby aggregations |
| matplotlib | Static chart generation |
| numpy | Random number generation for synthetic data |
| GitHub | Version control and portfolio hosting |

---

## 📦 Dataset

| Attribute | Value |
|-----------|-------|
| Period | January 1 – March 31, 2023 (91 days) |
| Transactions | ~5,000–9,000 rows (20–100 per day, randomly generated) |
| Products | 10 items across beverages and food |
| Columns | `Date`, `Item`, `Quantity`, `Price`, `Total` |

**Product catalogue:**

| Category | Items | Price Range |
|----------|-------|------------|
| Espresso-based | Espresso, Americano | $2.00 – $5.00 |
| Milk-based | Latte, Cappuccino, Mocha | $3.00 – $6.00 |
| Other drinks | Tea | $2.00 – $5.00 |
| Food | Pastry, Sandwich, Cake, Cookie | $1.50 – $4.00 |

---

## 🔍 Key Findings

### 💰 1. Total Revenue: $59,989.21

Three months of trading generated just under **$60,000 in revenue**, averaging **$666.55 per day** across 91 days.

---

### 📅 2. Monthly Breakdown

| Month | Revenue | Note |
|-------|---------|------|
| January 2023 | **$20,542.54** | Highest month |
| February 2023 | **$19,451.77** | Slight dip — 28-day month |
| March 2023 | **$19,994.90** | Recovering trend |

> **Insight:** Revenue is remarkably stable — less than **$1,100 spread** across all three months. The February dip is likely explained by it being a shorter month (28 vs 31 days), not a demand drop.

---

### ☕ 3. Top 5 Items by Revenue

| Rank | Item | Revenue |
|------|------|---------|
| 🥇 1 | Latte | **$8,063.68** |
| 🥈 2 | Cappuccino | **$7,765.37** |
| 🥉 3 | Mocha | **$7,680.90** |
| 4 | Americano | — |
| 5 | Espresso | — |

> **Insight:** Latte, Cappuccino, and Mocha together account for ~**39% of total revenue** from just 3 of 10 products. These are non-negotiable core stock items.

---

### 📦 4. Top Items by Units Sold

| Rank | Item | Units Sold |
|------|------|-----------|
| 🥇 1 | Pastry | **1,769** |
| 🥈 2 | Latte | **1,765** |
| 3 | Cappuccino | — |
| 4 | Cookie | — |
| 5 | Sandwich | — |

> **Insight:** Pastry leads in volume but doesn't appear in the top revenue list — classic **high volume, low margin** product. Latte is the only item in the top 2 of *both* lists, making it the single most important SKU.

---

### 📆 5. Peak vs. Slowest Day

| | Date | Revenue |
|---|------|---------|
| 🔝 **Peak Day** | February 28, 2023 | **$1,143.96** |
| 🔻 **Slowest Day** | January 11, 2023 | **$152.60** |

> The best day outperformed the worst by nearly **7.5x**. This level of day-to-day variance suggests that mid-week or early-January targeted promotions could significantly lift the floor.

---

### 📈 6. Daily Sales Trend

- Day-to-day fluctuation is high, but a **gentle upward slope is visible through March**
- Mid-week days consistently trail Friday and Monday
- No single sustained dip — the business is operationally stable

---

## 💡 Business Recommendations

| Priority | Recommendation | Data Behind It |
|----------|---------------|---------------|
| 🔴 High | Never stock out of Latte, Cappuccino, Mocha | Top 3 revenue items |
| 🔴 High | Bundle Pastry with a drink ("Coffee + Pastry deal") | Pastry: most units sold, lowest per-unit revenue |
| 🟡 Medium | Run mid-week promotions to lift slow days like Jan 11 | $991 gap between peak and slowest day |
| 🟡 Medium | Check whether Feb dip was calendar-driven or demand-driven | Shortest month = fewer trading days |
| 🟢 Low | Evaluate Sandwich — low volume and low revenue vs food peers | Possible cut or recipe/pricing review |

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Badger-analyst/Coffee-Shop-sales-Analysis.git
cd Coffee-Shop-sales-Analysis
```

### 2. Install dependencies
```bash
pip install pandas matplotlib numpy
```

### 3. Generate the dataset
```bash
python generate_data.py
# Creates: data/sales_data.csv
```

### 4. Run the analysis
```bash
python analysis.py
# Prints metrics to terminal + saves 3 charts to images/
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---------|-----|
| `FileNotFoundError: data/sales_data.csv` | Run `python generate_data.py` first |
| Charts not saving | Ensure `images/` folder exists: `mkdir images` |
| `ModuleNotFoundError` | Run `pip install pandas matplotlib numpy` |
| Different numbers on each run | Expected — data is random. Add `random.seed(42)` to `generate_data.py` for reproducibility |

---

## 🚀 Planned Improvements

- [ ] Add `random.seed(42)` for fully reproducible results
- [ ] Add seaborn for richer visualisations
- [ ] Build a **linear regression model** to forecast April revenue
- [ ] Export a PDF summary report using `reportlab`
- [ ] Replace synthetic data with a real dataset from Kaggle

---

## 👤 About

Built by **[@Badger-analyst](https://github.com/Badger-analyst)** as a Python data analytics portfolio project.  
Skills demonstrated: data generation · cleaning · EDA · visualisation · business storytelling.

---

*⭐ If you found this useful, feel free to star the repo!*
