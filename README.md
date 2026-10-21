# 📊 Vendor Performance Analysis

## 📌 Project Overview

This project analyzes vendor performance, purchasing patterns, sales,
profitability, and inventory management using Python, SQL, and PostgreSQL.

The objective is to transform raw business data into meaningful insights
that can help businesses evaluate vendor contributions, understand
purchasing efficiency, and make better inventory and procurement decisions.

## 🎯 Business Objectives

- Analyze vendor and brand performance.
- Examine purchasing and sales patterns.
- Evaluate gross profit and profit margins.
- Understand stock turnover and inventory efficiency.
- Identify potential inventory and purchasing inefficiencies.
- Prepare data for future interactive visualization using Power BI.

## 🛠️ Tools & Technologies

- **Python** — Data analysis and processing
- **Pandas & NumPy** — Data manipulation
- **PostgreSQL** — Database management and querying
- **SQL** — Data aggregation and analysis
- **SQLAlchemy** — Python–database connectivity
- **Matplotlib & Seaborn** — Exploratory data visualization
- **Jupyter Notebook** — Interactive analysis
- **Power BI** — Planned dashboard development

## 📂 Project Structure

```text
Vendor-Performance-Analysis/
│
├── EDA/
│   ├── database_check.py
│   ├── summry_queries.py
│   └── vendor_sales_summry.py
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   └── ...
│
├── analysis.ipynb
├── connect_db.py
├── .gitignore
└── README.md
```

## 🔄 Project Workflow

### 1. Data Loading

Loaded business datasets containing inventory, purchases, and product
pricing information.

### 2. Database Setup

Used PostgreSQL to store and manage the datasets and Python with
SQLAlchemy to connect to the database.

### 3. SQL Analysis

Worked with SQL queries to organize and analyze the data.

Created a consolidated `vendor_sales_summary` table for vendor-level
performance analysis.

### 4. Exploratory Data Analysis (EDA)

Used Python and Pandas to explore the data and examine:

- Summary statistics
- Numerical distributions
- Sales and purchasing quantities
- Gross profit and profit margin
- Stock turnover
- Sales-to-purchase ratio

Used Matplotlib and Seaborn for data visualization.

### 5. Vendor Performance Analysis

Explored vendor and brand performance using purchasing, sales, and
profitability-related metrics to understand differences in business
performance.

### 6. Future Development

The next phase is to develop an interactive Power BI dashboard to
present key metrics, comparisons, and business insights.

## 📈 Key Metrics

| Metric | Purpose |
|---|---|
| Gross Profit | Evaluates profitability |
| Profit Margin | Measures profit relative to sales |
| Stock Turnover | Helps evaluate inventory movement |
| Sales-to-Purchase Ratio | Compares sales and purchasing quantities |

## 📊 Expected Business Value

The analysis aims to help businesses:

- Compare vendor contributions.
- Understand purchasing and sales patterns.
- Evaluate vendor profitability.
- Identify potential inventory inefficiencies.
- Support data-driven procurement decisions.

## 📁 Dataset Note

The `purchases.csv` file is not included in this GitHub repository
because it exceeds GitHub's standard 100 MB file-size limit.

The original file remains available locally to the project owner.

Other datasets included in the repository should be checked for
availability and completeness before running the analysis.

## 🚀 Future Improvements

- Develop an interactive Power BI dashboard.
- Add vendor performance rankings.
- Expand profitability and inventory analysis.
- Document validated findings and actionable recommendations.

## 👩‍💻 Author

**Mansi Jaiswal**

B.Tech Computer Science Engineering
