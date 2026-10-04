"""Pandas basics: load, clean, and answer simple business questions from sales.csv"""
import pandas as pd

# 1. Load the data
df = pd.read_csv("sales.csv", parse_dates=["order_date"])
print("Rows:", len(df))
print(df.head())

# 2. Clean it
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

print("Missing values per column:\n", df.isna().sum())
df["city"] = df["city"].fillna("Unknown")

# 3. Add a revenue column
df["revenue"] = df["quantity"] * df["unit_price"]

# 4. Answer questions
print("\nTotal revenue:", df["revenue"].sum())

print("\nRevenue by category:")
print(df.groupby("category")["revenue"].sum().sort_values(ascending=False))

print("\nRevenue by city:")
print(df.groupby("city")["revenue"].sum().sort_values(ascending=False))

print("\nTop 3 products by revenue:")
print(df.groupby("product")["revenue"].sum().nlargest(3))

df["month"] = df["order_date"].dt.to_period("M")
print("\nRevenue by month:")
print(df.groupby("month")["revenue"].sum())
