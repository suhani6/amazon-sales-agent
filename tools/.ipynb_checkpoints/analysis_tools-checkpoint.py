import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("../data/clean_amazon_sales.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

# 1. Total Revenue by Month
def get_total_revenue_by_month():
    monthly_revenue = df.resample('M', on='order_date')['total_sales'].sum()
    return monthly_revenue

# 2. Top N Products by Total Sales
def get_top_n_products(n=5):
    top_products = df.groupby('product_name')['total_sales'].sum().nlargest(n)
    return top_products

# 3. Plot Monthly Revenue Trend
def plot_monthly_revenue_trend():
    monthly = df.resample('M', on='order_date')['total_sales'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(monthly.index, monthly.values, marker='o')
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("monthly_revenue_trend.png")
    return "Chart saved as monthly_revenue_trend.png"

# 4. Average Profit by Region
def get_average_profit_by_region():
    avg_profit = df.groupby('region')['profit_margin'].mean().sort_values(ascending=False)
    return avg_profit

# 5. Sales by Category
def get_sales_by_category():
    sales_by_cat = df.groupby('product_category')['total_sales'].sum().sort_values(ascending=False)
    return sales_by_cat

# 6. Plot Category Distribution
def plot_category_distribution():
    category_counts = df['product_category'].value_counts()
    plt.figure(figsize=(8, 6))
    category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Product Category Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("category_distribution.png")
    return "Chart saved as category_distribution.png"

# 7. Order Status Breakdown
def get_order_status_breakdown():
    return df['order_status'].value_counts()
