import streamlit as st
from snowflake.snowpark import Session
from groq import Groq

st.set_page_config(page_title="Econ Agent Dashboard", layout="wide")

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

import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_session():
    try:
        session = Session.builder.configs(connection_params).create()
        return session
    except Exception as e:
        st.error("Connection Failed")
        st.exception(e)
        st.stop()

session = get_session()

st.sidebar.title("Econ Agent")
st.sidebar.success("Connected to Snowflake")

page = st.sidebar.radio("Navigate", ["Home", "Browse Tables", "Run Query", "AI Assistant"])

def get_tables():
    try:
        result = session.sql("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'ANALYTICS'").collect()
        return [row["TABLE_NAME"] for row in result]
    except Exception as e:
        st.error("Could not fetch tables")
        st.exception(e)
        return []

if page == "Home":
    st.title("Econ Agent Dashboard")
    st.markdown("Welcome! Use the sidebar to explore your data or chat with the AI assistant.")
    tables = get_tables()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Database", "ECON_AGENT_DB")
    with col2:
        st.metric("Schema", "ANALYTICS")
    with col3:
        st.metric("Tables Found", len(tables))
    if tables:
        st.subheader("Available Tables")
        for t in tables:
            st.write(f"- {t}")

elif page == "Browse Tables":
    st.title("Browse Tables")
    tables = get_tables()
    if not tables:
        st.warning("No tables found in ANALYTICS schema.")
    else:
        selected_table = st.selectbox("Select a table to preview", tables)
        row_limit = st.slider("Number of rows to preview", 10, 500, 50)
        if st.button("Load Table"):
            try:
                df = session.sql(f"SELECT * FROM {selected_table} LIMIT {row_limit}").to_pandas()
                st.success(f"Showing {len(df)} rows from {selected_table}")
                st.dataframe(df, use_container_width=True)
                st.subheader("Basic Statistics")
                st.dataframe(df.describe(), use_container_width=True)
            except Exception as e:
                st.error("Failed to load table")
                st.exception(e)

elif page == "Run Query":
    st.title("Run a SQL Query")
    query = st.text_area("Enter your SQL query", value="SELECT * FROM ANALYTICS.YOUR_TABLE LIMIT 10", height=150)
    if st.button("Run Query"):
        if query.strip() == "":
            st.warning("Please enter a query.")
        else:
            try:
                with st.spinner("Running query..."):
                    df = session.sql(query).to_pandas()
                st.success(f"Query returned {len(df)} rows")
                st.dataframe(df, use_container_width=True)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(label="Download as CSV", data=csv, file_name="query_results.csv", mime="text/csv")
            except Exception as e:
                st.error("Query failed")
                st.exception(e)

elif page == "AI Assistant":
    st.title("AI Assistant (Groq)")
    st.markdown("Ask questions about economics or your data.")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    if prompt := st.chat_input("Ask something..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are a helpful economics data assistant."},
                            *st.session_state.messages
                        ],
                       model="llama-3.3-70b-versatile",
                    )
                    response = chat_completion.choices[0].message.content
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error("AI response failed.")
                    st.exception(e)
                    
