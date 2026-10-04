# Data Analyst Practice (Python + SQL)

Small, beginner-friendly scripts for analysing a sales table.

**Data:** `sales.csv` is a small made-up dataset (29 orders, Jan-Jun 2025) written by hand for practice. It includes one duplicate row and one missing city on purpose, so the cleaning step has something to do.

| File | What it shows |
|---|---|
| `01_pandas_basics.py` | Load, remove duplicates, fill missing values, `groupby`, top-N, monthly totals |
| `02_sql_queries.py` | `GROUP BY`, `HAVING`, date functions, CTE, `LAG`, `RANK` on the same data via SQLite |
| `03_chart.py` | A bar chart saved as PNG with matplotlib |

## Run

```bash
pip install pandas matplotlib
python 01_pandas_basics.py
python 02_sql_queries.py
python 03_chart.py
```
