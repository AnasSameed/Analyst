"""SQL basics: load sales.csv into a SQLite table and query it with plain SQL."""
import sqlite3

import pandas as pd

df = pd.read_csv("sales.csv").drop_duplicates()
conn = sqlite3.connect(":memory:")
df.to_sql("sales", conn, index=False)


def run(title, sql):
    print(f"\n--- {title} ---")
    print(pd.read_sql(sql, conn).to_string(index=False))


run("Revenue by category", """
    SELECT category, SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
""")

run("Cities with more than 5 orders", """
    SELECT city, COUNT(*) AS orders
    FROM sales
    GROUP BY city
    HAVING COUNT(*) > 5
""")

run("Monthly revenue", """
    SELECT strftime('%Y-%m', order_date) AS month,
           SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month
""")

run("Month-over-month change (window function)", """
    WITH monthly AS (
        SELECT strftime('%Y-%m', order_date) AS month,
               SUM(quantity * unit_price) AS revenue
        FROM sales
        GROUP BY month
    )
    SELECT month, revenue,
           revenue - LAG(revenue) OVER (ORDER BY month) AS change_from_last_month
    FROM monthly
""")

run("Rank products inside each category", """
    SELECT category, product, SUM(quantity * unit_price) AS revenue,
           RANK() OVER (PARTITION BY category ORDER BY SUM(quantity * unit_price) DESC) AS rank_in_category
    FROM sales
    GROUP BY category, product
""")
