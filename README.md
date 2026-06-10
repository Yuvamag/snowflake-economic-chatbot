# Snowflake Economic Analytics Chatbot

## Project Overview

This project demonstrates an end-to-end data engineering and analytics workflow using Snowflake, Snowpark, Dynamic Tables, Streamlit, and Generative AI.

The solution combines multiple US economic datasets into a single analytics layer and provides an interactive dashboard along with an AI-powered chatbot for exploring economic trends.

The project uses public datasets available in Snowflake and focuses on analyzing:

- Consumer Price Index (CPI)
- Unemployment Rate
- 30-Year Fixed Mortgage Rate

---

## Problem Statement

Economic indicators are often spread across multiple datasets, making it difficult to perform unified analysis and generate insights efficiently.

Analysts typically spend time locating datasets, performing transformations, combining metrics, and refreshing reports manually.

This project addresses that challenge by:

- Integrating multiple public economic datasets
- Automating data preparation using Snowpark
- Creating a continuously refreshed Dynamic Table
- Providing a user-friendly analytics dashboard
- Enabling natural-language interaction through an AI chatbot

The result is a centralized platform for exploring economic trends and answering business questions using real-world data.

---

## Learning Objectives

This project was built as part of my hands-on learning journey with Snowflake.

The primary goals were to gain practical experience with:

- Snowflake Architecture
- Snowflake Public Data Products
- Snowpark for Python
- Dynamic Tables
- Streamlit Integration
- Data Validation Techniques
- AI-Powered Analytics Applications

Through this project, I explored how modern cloud data platforms can be used to ingest, transform, automate, and serve analytical data products.

---

## Technologies Used

### Data Platform
- Snowflake

### Data Engineering
- Snowpark for Python
- Dynamic Tables
- SQL

### Application Layer
- Streamlit

### AI Integration
- Groq API
- Llama 3.3 70B Model

### Programming Language
- Python

---

## Data Sources

### Financial Economic Indicators

Dataset:

`SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES`

Used to retrieve:

- Consumer Price Index (CPI)
- Unemployment Rate

### Freddie Mac Housing Data

Dataset:

`SNOWFLAKE_PUBLIC_DATA_FREE.PUBLIC_DATA_FREE.FREDDIE_MAC_HOUSING_TIMESERIES`

Used to retrieve:

- 30-Year Fixed Mortgage Rate

---

## Solution Architecture

```text
Snowflake Public Data
            │
            ▼
    Snowpark Transformations
            │
            ▼
    Combined Economic Dataset
            │
            ▼
      Dynamic Table
            │
            ▼
      Validation Layer
            │
            ▼
      Streamlit Dashboard
            │
            ▼
       AI Chatbot (Groq)
```

---

## Project Workflow

### 1. Data Exploration

Public economic datasets were explored using Snowflake SQL to identify relevant indicators.

### 2. Data Extraction

Snowpark DataFrames were used to extract:

- CPI
- Unemployment Rate
- Mortgage Rate

from separate Snowflake Public Data tables.

### 3. Data Transformation

The datasets were combined into a unified structure and pivoted into an analytics-friendly format.

### 4. Dashboard Dataset Creation

A Snowflake table was created to store the transformed economic indicators.

### 5. Dynamic Table Creation

A Dynamic Table was implemented to automatically refresh economic metrics on a scheduled basis.

### 6. Validation

Validation queries were performed to verify:

- Row counts
- Date ranges
- Null values
- Refresh status
- Metric completeness

### 7. Streamlit Application

A Streamlit application was developed to:

- Browse tables
- Run SQL queries
- View dataset previews
- Download query results

### 8. AI Assistant

A chatbot powered by Groq and Llama 3.3 was integrated to answer user questions related to economics and data analysis.

---

## Repository Structure

```text
Snowflake-Economic-Analytics-Chatbot/
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_explore_data.sql
│   ├── 03_create_dynamic_table.sql
│   └── 04_validation.sql
│
├── python/
│   ├── economic_dashboard.py
│   └── chatbot_app.py
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Key Snowflake Features Demonstrated

- Snowflake Public Data Products
- Snowpark DataFrames
- SQL Analytics
- Dynamic Tables
- Automated Data Refresh
- Streamlit Integration
- Data Validation
- AI-Driven Analytics

---

## Screenshots

### Snowflake Data Exploration

Add screenshot here.

### Dynamic Table Creation

Add screenshot here.

### Validation Results

Add screenshot here.

### Streamlit Dashboard

Add screenshot here.

### AI Chatbot

Add screenshot here.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Snowflake-Economic-Analytics-Chatbot.git
```

Move into the project directory:

```bash
cd Snowflake-Economic-Analytics-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the project, update the Snowflake connection parameters and API credentials:

```python
connection_params = {
    "account": "<YOUR_SNOWFLAKE_ACCOUNT>",
    "user": "<YOUR_SNOWFLAKE_USERNAME>",
    "password": "<YOUR_SNOWFLAKE_PASSWORD>",
    "role": "<YOUR_ROLE>",
    "warehouse": "<YOUR_WAREHOUSE>",
    "database": "<YOUR_DATABASE>",
    "schema": "<YOUR_SCHEMA>"
}
```

```python
GROQ_API_KEY = "<YOUR_GROQ_API_KEY>"
```

---

## Run the Application

```bash
streamlit run chatbot_app.py
```

---

## Future Improvements

- Add additional economic indicators
- Create advanced visualizations
- Implement role-based access control
- Integrate Snowflake Cortex models
- Add forecasting and trend analysis
- Deploy the application to the cloud

---

## Author

Built as a hands-on Snowflake learning project focused on modern data engineering, analytics, and AI integration.
