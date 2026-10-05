from dotenv import load_dotenv
import os
import pyodbc
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")

from sqlalchemy.engine import URL

load_dotenv()

#server = os.getenv("SQL_SERVER")
#database = os.getenv("SQL_DATABASE")
#username = os.getenv("SQL_USERNAME")
#password = os.getenv("SQL_PASSWORD")


connection_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host="localhost",
    port=1433,
    database=database,
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes"
    }
)

engine = create_engine(connection_url)


def execute_query(query):
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    return df


def get_schema(table_name):
    query = f"""
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = '{table_name}'
    ORDER BY ORDINAL_POSITION
    """

    return execute_query(query)

#result = get_schema("orders")

#print(result)