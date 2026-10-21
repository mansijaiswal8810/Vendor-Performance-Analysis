# ============================================================
# DATABASE CHECK
# ============================================================

import pandas as pd
from sqlalchemy import create_engine
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
# 2. CHECK DATABASE CONNECTION & AVAILABLE TABLES
# ============================================================

# Check all tables available in the PostgreSQL database

tables = pd.read_sql("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""", engine)

print(tables)


# ============================================================
# 3. CHECK RECORD COUNT AND SAMPLE DATA
# ============================================================

# Check the number of records and first 5 rows of each table

for table in tables['table_name']:

    print('-' * 50, f'{table}', '-' * 50)

    print(
        f'Count of records: ',
        pd.read_sql(
            f"select count(*) as count from {table}",
            engine
        )['count'].values[0]
    )

    print(
        pd.read_sql(
            f"select * from {table} limit 5",
            engine
        )
    )

