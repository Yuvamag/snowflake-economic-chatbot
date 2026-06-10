USE DATABASE ECON_AGENT_DB;
USE SCHEMA ANALYTICS;

-- =====================================================
-- VALIDATION 1: Verify Dynamic Table Exists
-- =====================================================

SHOW DYNAMIC TABLES LIKE 'ECONOMIC_DASHBOARD_LIVE';

-- =====================================================
-- VALIDATION 2: Total Row Count
-- =====================================================

SELECT COUNT(*) AS TOTAL_ROWS
FROM ECONOMIC_DASHBOARD_LIVE;

-- =====================================================
-- VALIDATION 3: Date Range
-- =====================================================

SELECT
    MIN(DATE) AS FIRST_DATE,
    MAX(DATE) AS LAST_DATE
FROM ECONOMIC_DASHBOARD_LIVE;

-- =====================================================
-- VALIDATION 4: Latest Records
-- =====================================================

SELECT *
FROM ECONOMIC_DASHBOARD_LIVE
ORDER BY DATE DESC
LIMIT 10;

-- =====================================================
-- VALIDATION 5: Null Analysis
-- =====================================================

SELECT
    COUNT(*) AS TOTAL_ROWS,
    COUNT(CPI) AS CPI_ROWS,
    COUNT(UNEMPLOYMENT_RATE) AS UNEMPLOYMENT_ROWS,
    COUNT(MORTGAGE_RATE_30Y) AS MORTGAGE_ROWS
FROM ECONOMIC_DASHBOARD_LIVE;

-- =====================================================
-- VALIDATION 6: Duplicate Date Check
-- =====================================================

SELECT
    DATE,
    COUNT(*) AS RECORD_COUNT
FROM ECONOMIC_DASHBOARD_LIVE
GROUP BY DATE
HAVING COUNT(*) > 1;

-- =====================================================
-- VALIDATION 7: Data Quality Check
-- =====================================================

SELECT
    MIN(CPI) AS MIN_CPI,
    MAX(CPI) AS MAX_CPI,
    MIN(UNEMPLOYMENT_RATE) AS MIN_UNEMPLOYMENT_RATE,
    MAX(UNEMPLOYMENT_RATE) AS MAX_UNEMPLOYMENT_RATE,
    MIN(MORTGAGE_RATE_30Y) AS MIN_MORTGAGE_RATE,
    MAX(MORTGAGE_RATE_30Y) AS MAX_MORTGAGE_RATE
FROM ECONOMIC_DASHBOARD_LIVE;

-- =====================================================
-- VALIDATION 8: Latest CPI Values
-- =====================================================

SELECT
    DATE,
    CPI
FROM ECONOMIC_DASHBOARD_LIVE
WHERE CPI IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 9: Latest Unemployment Values
-- =====================================================

SELECT
    DATE,
    UNEMPLOYMENT_RATE
FROM ECONOMIC_DASHBOARD_LIVE
WHERE UNEMPLOYMENT_RATE IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 10: Latest Mortgage Values
-- =====================================================

SELECT
    DATE,
    MORTGAGE_RATE_30Y
FROM ECONOMIC_DASHBOARD_LIVE
WHERE MORTGAGE_RATE_30Y IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 11: Source vs Dashboard (CPI)
-- =====================================================

SELECT
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES
WHERE GEO_ID = 'country/USA'
AND VARIABLE_NAME =
'CPI: All items, Monthly, 1982-84 Index Date (Seasonally adjusted)'
ORDER BY DATE DESC
LIMIT 5;

SELECT
    DATE,
    CPI
FROM ECONOMIC_DASHBOARD_LIVE
WHERE CPI IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 12: Source vs Dashboard (Unemployment)
-- =====================================================

SELECT
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES
WHERE GEO_ID = 'country/USA'
AND VARIABLE_NAME =
'Current Labor Force: Unemployment Rate - 20 yrs. & over, Monthly (Seasonally adjusted)'
ORDER BY DATE DESC
LIMIT 5;

SELECT
    DATE,
    UNEMPLOYMENT_RATE
FROM ECONOMIC_DASHBOARD_LIVE
WHERE UNEMPLOYMENT_RATE IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 13: Source vs Dashboard (Mortgage Rate)
-- =====================================================

SELECT
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FREDDIE_MAC_HOUSING_TIMESERIES
WHERE VARIABLE_NAME =
'30-Year Fixed Rate Mortgage Rate, National Average'
ORDER BY DATE DESC
LIMIT 5;

SELECT
    DATE,
    MORTGAGE_RATE_30Y
FROM ECONOMIC_DASHBOARD_LIVE
WHERE MORTGAGE_RATE_30Y IS NOT NULL
ORDER BY DATE DESC
LIMIT 5;

-- =====================================================
-- VALIDATION 14: Dynamic Table Refresh Metadata
-- =====================================================

SHOW DYNAMIC TABLES LIKE 'ECONOMIC_DASHBOARD_LIVE';
