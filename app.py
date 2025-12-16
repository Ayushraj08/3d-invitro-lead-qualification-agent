import streamlit as st
import pandas as pd
from scoring import process_leads

# Page configuration
st.set_page_config(
    page_title="3D In-Vitro Lead Qualification",
    layout="wide"
)

# Header
st.title("3D In-Vitro Lead Qualification Dashboard")
st.write(
    "This dashboard identifies, enriches, and ranks life-science professionals "
    "based on their probability of adopting **3D in-vitro models** for drug discovery "
    "and safety assessment."
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/leads_raw.csv")

raw_df = load_data()

# Process leads
scored_df = process_leads(raw_df)

# Filters
st.subheader("Filter Qualified Leads")

search_query = st.text_input(
    "Search by Name, Title, Company, Location, or Source"
)

min_score = st.slider(
    "Minimum Probability Score",
    min_value=0,
    max_value=100,
    value=0
)

filtered_df = scored_df[scored_df["probability_score"] >= min_score]

if search_query:
    q = search_query.lower()
    filtered_df = filtered_df[
        filtered_df.apply(
            lambda row: q in " ".join(row.astype(str).str.lower()),
            axis=1
        )
    ]

# Display table
st.subheader("Ranked Lead List")

display_columns = [
    "rank",
    "probability_score",
    "name",
    "title",
    "company",
    "person_location",
    "company_hq",
    "is_remote",
    "email",
    "source"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True
)

# Download option
st.download_button(
    label="Download Qualified Leads (CSV)",
    data=filtered_df.to_csv(index=False),
    file_name="qualified_leads.csv",
    mime="text/csv"
)

# Footer / disclaimer
st.markdown("---")
st.caption(
    "Disclaimer: Data used in this demo is simulated for demonstration purposes. "
    "The scoring logic reflects a production-ready business development "
    "prioritization model."
)
