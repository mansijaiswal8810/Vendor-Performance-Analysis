# ============================================================
# CONNECT DATABASE & LOAD RAW DATA
# ============================================================

# Import required libraries
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.engine import URL

# ============================================================
# 1. POSTGRESQL DATABASE CONNECTION
# ============================================================

# Create a connection between Python and PostgreSQL.
# Database: inventory
# Host: localhost
# Port: 5432

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
# 2. DATABASE INGESTION FUNCTION
# ============================================================

# This function uploads a Pandas DataFrame
# into a PostgreSQL table.

def ingest_db(df, table_name, engine):

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=5000
    )


# ============================================================
# 3. LOAD RAW CSV DATA
# ============================================================

# This function reads all CSV files from the data folder
# and uploads them into PostgreSQL.

def load_raw_data():

    # Loop through all files present inside the data folder
    for file in os.listdir("data"):

        # Process only CSV files
        if file.endswith(".csv"):

            print(f"Uploading {file}...")

            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv("data/" + file)

            # Remove ".csv" extension to create table name
            table_name = file[:-4]

            # Upload DataFrame to PostgreSQL
            ingest_db(df, table_name, engine)

            print(f"{file} uploaded successfully!")


# ============================================================
# 4. PROGRAM EXECUTION
# ============================================================

# Run the data-loading process when this file
# is executed directly.

if __name__ == "__main__":
    load_raw_data()