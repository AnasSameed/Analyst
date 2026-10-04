"""One simple chart: revenue by category, saved as a PNG."""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales.csv").drop_duplicates()
df["revenue"] = df["quantity"] * df["unit_price"]

revenue = df.groupby("category")["revenue"].sum().sort_values()

plt.figure(figsize=(6, 3.5))
plt.barh(revenue.index, revenue.values, color="#2a78d6")
plt.xlabel("Revenue (INR)")
plt.title("Revenue by category")
plt.tight_layout()
plt.savefig("revenue_by_category.png", dpi=150)
print("Saved revenue_by_category.png")
