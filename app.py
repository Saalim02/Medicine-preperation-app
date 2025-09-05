import streamlit as st
import pandas as pd

# Load Excel
df = pd.read_excel("Y-Unani_medicines.xlsx")
df.columns = df.columns.str.strip()  # remove extra spaces

st.title("Unani Medicine Explorer 🌿")

# Search by Medicine Name
search_term = st.text_input("Search for medicine:")
if search_term:
    filtered_df = df[df['Medicine Name'].str.contains(search_term, case=False)]
else:
    filtered_df = df

# Optional: Filter by Therapeutic uses
therapeutic_filter = st.multiselect(
    "Filter by Therapeutic uses:",
    options=df['Therapeutic uses'].dropna().unique()
)
if therapeutic_filter:
    filtered_df = filtered_df[filtered_df['Therapeutic uses'].isin(therapeutic_filter)]

# Display table
st.dataframe(filtered_df)
