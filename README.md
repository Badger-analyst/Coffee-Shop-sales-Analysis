# Coffee Shop Sales Analysis

## Project Overview
This dummy project analyzes 3 months (Jan-Mar 2023) of simulated coffee shop sales data. It demonstrates data generation, cleaning, exploratory data analysis (EDA), and visualization using Python (pandas, matplotlib). Built as a portfolio piece to showcase data skills for recruiters.

### Objectives
- Generate realistic sales data.
- Calculate total/monthly revenue, top items, average daily sales, and peak/slowest days.
- Provide insights for business decisions (e.g., stock popular items).
- Visualize trends.

### Data Source
- `data/sales_data.csv`: Generated via `generate_data.py` (randomized for realism; ~5,000-9,000 transactions).
- Columns: Date, Item, Quantity, Price, Total.

### Methodology
1. **Data Generation**: Used random values for daily transactions (20-100), quantities (1-5), and prices based on item type.
2. **Cleaning**: Removed invalid entries (e.g., negative totals).
3. **Analysis**: Aggregated by month/item/date using pandas.
4. **Visualization**: Bar/pie/line plots saved to `images/`.

Run `python analysis.py` to reproduce.

## Key Findings
- **Total Revenue**: $59,989.21 over 3 months.
- **Monthly Breakdown**:
  | Month   | Revenue ($) |
  |---------|-------------|
  | 2023-01 | 20,542.54  |
  | 2023-02 | 19,451.77  |
  | 2023-03 | 19,994.90  |

  ![Monthly Sales](images/monthly_sales.png)

- **Top Items by Revenue**:
  | Item       | Revenue ($) |
  |------------|-------------|
  | Latte      | 8,063.68   |
  | Cappuccino | 7,765.37   |
  | Mocha      | 7,680.90   |
  | ... (full list in analysis.py output) |

  ![Top Items Revenue](images/top_items_revenue.png)

- **Top Items by Quantity**:
  | Item    | Quantity |
  |---------|----------|
  | Pastry  | 1,769   |
  | Latte   | 1,765   |
  | ...     | ...     |

- **Average Daily Sales**: $666.55.
- **Peak Day**: Feb 28, 2023 ($1,143.96) – Possibly due to end-of-month promotions.
- **Slowest Day**: Jan 11, 2023 ($152.60) – Mid-week lull; suggest targeted marketing.
- **Daily Trend**: Sales fluctuate but show slight growth in March.

  ![Daily Sales Trend](images/daily_sales_trend.png)

## Insights & Recommendations
- Beverages (Latte, Cappuccino, Mocha) drive ~40% of revenue – Focus inventory here.
- Food items have high quantity but lower per-unit price – Bundle with drinks for upselling.
- Monthly stability with minor dip in Feb – Investigate seasonal factors.
- To improve: Add real data, machine learning for forecasting, or SQL for querying.

## Tools Used
- Python: pandas for analysis, matplotlib for plots.
- GitHub for version control.

## How to Run
1. Clone repo.
2. Run `python generate_data.py`.
3. Run `python analysis.py`.

Contact: [Your LinkedIn/Email]. Open to feedback!