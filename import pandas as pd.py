import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define the period: 3 months, Jan to Mar 2023
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 3, 31)
date_range = pd.date_range(start=start_date, end=end_date)

# Coffee shop items with approximate price ranges
items = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Tea', 'Pastry', 'Sandwich', 'Cake', 'Cookie']

# Generate sample data
data = []
for date in date_range:
    num_sales = random.randint(20, 100)  # Daily transactions
    for _ in range(num_sales):
        item = random.choice(items)
        quantity = random.randint(1, 5)
        # Assign prices based on item type
        if item in ['Espresso', 'Americano', 'Tea']:
            price = round(random.uniform(2.0, 5.0), 2)
        elif item in ['Latte', 'Cappuccino', 'Mocha']:
            price = round(random.uniform(3.0, 6.0), 2)
        else:
            price = round(random.uniform(1.5, 4.0), 2)
        total = round(quantity * price, 2)
        data.append([date.strftime('%Y-%m-%d'), item, quantity, price, total])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=['Date', 'Item', 'Quantity', 'Price', 'Total'])
df.to_csv('data/sales_data.csv', index=False)
print("CSV generated: data/sales_data.csv")