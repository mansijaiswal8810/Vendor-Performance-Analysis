# ============================================================
# VENDOR SALES SUMMARY
# ============================================================

import pandas as pd
from sqlalchemy import create_engine
import time
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL
# ============================================================
# 1. POSTGRESQL DATABASE CONNECTION
# ============================================================

load_dotenv()

engine = create_engine(
    URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=5432,
        database=os.getenv("DB_NAME")
    )
)

# ============================================================
# 2. CREATE FINAL VENDOR SALES SUMMARY
# ============================================================

start = time.time()

Vendor_Sales_Summary = pd.read_sql_query(
    """
    WITH FreightSummary AS (
        SELECT
            "VendorNumber",
            SUM("Freight") AS "FreightCost"
        FROM vendor_invoice
        GROUP BY "VendorNumber"
    ),

    PurchaseSummary AS (
        SELECT
            p."VendorNumber",
            p."VendorName",
            p."Brand",
            p."Description",
            p."PurchasePrice",
            pp."Price" AS "ActualPrice",
            pp."Volume",
            SUM(p."Quantity") AS "TotalPurchaseQuantity",
            SUM(p."Dollars") AS "TotalPurchaseDollars"
        FROM purchases p
        JOIN purchase_prices pp
            ON p."Brand" = pp."Brand"
        WHERE p."PurchasePrice" > 0
        GROUP BY
            p."VendorNumber",
            p."VendorName",
            p."Brand",
            p."Description",
            p."PurchasePrice",
            pp."Price",
            pp."Volume"
    ),

    SalesSummary AS (
        SELECT
            "VendorNo",
            "Brand",
            SUM("SalesQuantity") AS "TotalSalesQuantity",
            SUM("SalesDollars") AS "TotalSalesDollars",
            SUM("SalesPrice") AS "TotalSalesPrice",
            SUM("ExciseTax") AS "TotalExciseTax"
        FROM sales
        GROUP BY "VendorNo", "Brand"
    )

    SELECT
        ps.*,
        ss."TotalSalesQuantity",
        ss."TotalSalesDollars",
        ss."TotalSalesPrice",
        ss."TotalExciseTax",
        fs."FreightCost"
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps."VendorNumber" = ss."VendorNo"
        AND ps."Brand" = ss."Brand"
    LEFT JOIN FreightSummary fs
        ON ps."VendorNumber" = fs."VendorNumber"
    """,
    engine
)


# ============================================================
# 3. CHECK FINAL QUERY OUTPUT
# ============================================================

print(Vendor_Sales_Summary)

print("Time taken:", time.time() - start)

print(Vendor_Sales_Summary.dtypes)

print(Vendor_Sales_Summary.isnull().sum())


# ============================================================
# 4. DATA CLEANING
# ============================================================

# Replace missing values with 0

Vendor_Sales_Summary.fillna(0, inplace=True)


# Convert Volume column to float64

Vendor_Sales_Summary['Volume'] = (
    Vendor_Sales_Summary['Volume'].astype('float64')
)


# Remove leading and trailing spaces from VendorName

Vendor_Sales_Summary['VendorName'] = (
    Vendor_Sales_Summary['VendorName'].str.strip()
)


# ============================================================
# 5. VALIDATE CLEANED DATA
# ============================================================

print(Vendor_Sales_Summary.dtypes)

print(Vendor_Sales_Summary.isnull().sum())

print(Vendor_Sales_Summary['VendorName'].unique())


# ============================================================
# 6. CREATE BUSINESS METRICS
# ============================================================

# Gross Profit = Total Sales Dollars - Total Purchase Dollars

Vendor_Sales_Summary['GrossProfit'] = (
    Vendor_Sales_Summary['TotalSalesDollars']
    - Vendor_Sales_Summary['TotalPurchaseDollars']
)


# Profit Margin = Gross Profit / Total Sales Dollars × 100

Vendor_Sales_Summary['ProfitMargin'] = (
    Vendor_Sales_Summary['GrossProfit']
    / Vendor_Sales_Summary['TotalSalesDollars']
) * 100


# Stock Turnover = Total Sales Quantity / Total Purchase Quantity

Vendor_Sales_Summary['StockTurnover'] = (
    Vendor_Sales_Summary['TotalSalesQuantity']
    / Vendor_Sales_Summary['TotalPurchaseQuantity']
)


# Sales to Purchase Ratio = Total Sales Dollars / Total Purchase Dollars

Vendor_Sales_Summary['SalesToPurchaseRatio'] = (
    Vendor_Sales_Summary['TotalSalesDollars']
    / Vendor_Sales_Summary['TotalPurchaseDollars']
)


# ============================================================
# 7. FINAL CHECK
# ============================================================

print(Vendor_Sales_Summary.head())

print(Vendor_Sales_Summary.columns)


# ============================================================
# 8. SAVE FINAL SUMMARY TO POSTGRESQL
# ============================================================

Vendor_Sales_Summary.to_sql(
    'vendor_sales_summary',
    con=engine,
    if_exists='replace',
    index=False
)

print("vendor_sales_summary table created successfully!")