-- =====================================================
-- ECONOMIC DATA EXPLORATION
-- Snowflake Public Data Products
-- =====================================================

-- -----------------------------------------------------
-- Preview Economic Indicators Dataset
-- -----------------------------------------------------

SELECT *
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES
LIMIT 10;

-- -----------------------------------------------------
-- CPI (Inflation)
-- -----------------------------------------------------

SELECT
    VARIABLE_NAME,
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES
WHERE GEO_ID = 'country/USA'
  AND VARIABLE_NAME =
      'CPI: All items, Monthly, 1982-84 Index Date (Seasonally adjusted)'
ORDER BY DATE DESC
LIMIT 12;

-- -----------------------------------------------------
-- Unemployment Rate
-- -----------------------------------------------------

SELECT
    VARIABLE_NAME,
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES
WHERE GEO_ID = 'country/USA'
  AND VARIABLE_NAME =
      'Current Labor Force: Unemployment Rate - 20 yrs. & over, Monthly (Seasonally adjusted)'
ORDER BY DATE DESC
LIMIT 12;

-- -----------------------------------------------------
-- 30-Year Mortgage Rate
-- -----------------------------------------------------

SELECT
    VARIABLE_NAME,
    DATE,
    VALUE
FROM SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FREDDIE_MAC_HOUSING_TIMESERIES
WHERE VARIABLE_NAME =
      '30-Year Fixed Rate Mortgage Rate, National Average'
ORDER BY DATE DESC
LIMIT 12;
