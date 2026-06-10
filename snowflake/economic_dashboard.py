from snowflake.snowpark import Session
from snowflake.snowpark import functions as F
from snowflake.snowpark.types import DoubleType

# -----------------------------------
# Connect to Snowflake
# -----------------------------------

connection_params = {
    "account": "<YOUR_SNOWFLAKE_ACCOUNT>",
    "user": "<YOUR_SNOWFLAKE_USERNAME>",
    "password": "<YOUR_SNOWFLAKE_PASSWORD>",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "ECON_AGENT_DB",
    "schema": "ANALYTICS",
    "login_timeout": 10,
}

session = Session.builder.configs(connection_params).create()

print(
    "Connected!",
    session.sql(
        "SELECT CURRENT_USER(), CURRENT_WAREHOUSE()"
    ).collect()
)

# -----------------------------------
# Read Source Tables
# -----------------------------------

econ = session.table(
    "SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES"
)

housing = session.table(
    "SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FREDDIE_MAC_HOUSING_TIMESERIES"
)

# -----------------------------------
# CPI
# -----------------------------------

cpi = (
    econ.filter(F.col("GEO_ID") == "country/USA")
    .filter(
        F.col("VARIABLE_NAME")
        == "CPI: All items, Monthly, 1982-84 Index Date (Seasonally adjusted)"
    )
    .select(
        F.col("DATE"),
        F.col("VALUE").cast(DoubleType()).alias("VALUE"),
        F.lit("CPI").alias("METRIC"),
    )
)

print("CPI rows:", cpi.count())

# -----------------------------------
# Unemployment Rate
# -----------------------------------

unemployment = (
    econ.filter(F.col("GEO_ID") == "country/USA")
    .filter(
        F.col("VARIABLE_NAME")
        == "Current Labor Force: Unemployment Rate - 20 yrs. & over, Monthly (Seasonally adjusted)"
    )
    .select(
        F.col("DATE"),
        F.col("VALUE").cast(DoubleType()).alias("VALUE"),
        F.lit("UNEMPLOYMENT_RATE").alias("METRIC"),
    )
)

print("Unemployment rows:", unemployment.count())

# -----------------------------------
# Mortgage Rate
# -----------------------------------

mortgage = (
    housing.filter(
        F.col("VARIABLE_NAME")
        == "30-Year Fixed Rate Mortgage Rate, National Average"
    )
    .select(
        F.col("DATE"),
        F.col("VALUE").cast(DoubleType()).alias("VALUE"),
        F.lit("MORTGAGE_RATE_30Y").alias("METRIC"),
    )
)

print("Mortgage rows:", mortgage.count())

# -----------------------------------
# Combine Data
# -----------------------------------

combined = (
    cpi
    .union_all(unemployment)
    .union_all(mortgage)
)

print("\nCombined Sample:")
combined.show(20)

# -----------------------------------
# Pivot Dashboard
# -----------------------------------

dashboard = (
    combined
    .pivot(
        "METRIC",
        ["CPI", "UNEMPLOYMENT_RATE", "MORTGAGE_RATE_30Y"]
    )
    .agg(F.max("VALUE"))
    .sort(F.col("DATE").desc())
)

print("\nDashboard Preview:")
dashboard.show(20)

print(f"Total rows: {dashboard.count()}")
print(f"Columns: {dashboard.columns}")

# -----------------------------------
# Save as Snowflake Table
# -----------------------------------

dashboard.write.mode("overwrite").save_as_table(
    "ECONOMIC_DASHBOARD"
)

print("Table ECONOMIC_DASHBOARD created successfully!")

session.close()

print("Done!")
