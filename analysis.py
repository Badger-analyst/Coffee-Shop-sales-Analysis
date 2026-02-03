import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Data cleaning (example: check for negatives/missing values)
df = df[df['Total'] > 0]  # Remove any invalid totals
print(f"Data shape after cleaning: {df.shape}")

# Total sales
total_sales = df['Total'].sum()
print(f"Total sales over 3 months: ${total_sales:.2f}")

# Monthly sales
monthly_sales = df.groupby('Month')['Total'].sum()
print("\nMonthly sales:")
print(monthly_sales)
# Plot
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.ylabel('Total Revenue ($)')
plt.savefig('images/monthly_sales.png')
plt.close()

# Top items by revenue
item_revenue = df.groupby('Item')['Total'].sum().sort_values(ascending=False)
print("\nTop items by revenue:")
print(item_revenue)
# Plot top 5
item_revenue.head(5).plot(kind='pie', autopct='%1.1f%%', title='Top 5 Items by Revenue')
plt.savefig('images/top_items_revenue.png')
plt.close()

# Top items by quantity
item_qty = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False)
print("\nTop items by quantity:")
print(item_qty)

# Average daily sales
daily_sales = df.groupby('Date')['Total'].sum()
avg_daily = daily_sales.mean()
print(f"\nAverage daily sales: ${avg_daily:.2f}")

# Peak and slowest days
peak_day = daily_sales.idxmax().date()
peak_sales = daily_sales.max()
slow_day = daily_sales.idxmin().date()
slow_sales = daily_sales.min()
print(f"Peak day: {peak_day} with ${peak_sales:.2f}")
print(f"Slowest day: {slow_day} with ${slow_sales:.2f}")

# Daily sales trend plot
daily_sales.plot(title='Daily Sales Trend')
plt.ylabel('Revenue ($)')
plt.savefig('images/daily_sales_trend.png')
plt.close()