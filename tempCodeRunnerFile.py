import streamlit as st
import pandas as pd

# Load Excel
df = pd.read_excel("Y-Unani_medicines.xlsx")
df.columns = df.columns.str.strip()  # clean column names

st.title("Unani Medicine Guide 🌿")

# --- Step 0: Doctor enters medicine name ---
medicine_name = st.text_input("Enter medicine name:")

if medicine_name:
    # Filter the dataframe for that medicine
    medicine = df[df["Medicine Name"].str.contains(medicine_name, case=False, na=False)]

    if medicine.empty:
        st.error("❌ Medicine not found. Please try another name.")
    else:
        # Initialize step state
        if "step" not in st.session_state:
            st.session_state.step = 1

        # Step 1: Show Therapeutic uses
        if st.session_state.step == 1:
            st.subheader("Therapeutic Uses")
            st.write(medicine.iloc[0]["Therapeutic uses"])
            if st.button("Next ➡️"):
                st.session_state.step = 2
                st.rerun()

        # Step 2: Show Preparation method
        elif st.session_state.step == 2:
            st.subheader("Method of Preparation")
            st.write(medicine.iloc[0]["Method of preparation"])
            if st.button("Next ➡️"):
                st.session_state.step = 3
                st.rerun()

        # Step 3: Show Dosage
        elif st.session_state.step == 3:
            st.subheader("Dosage")
            st.write(medicine.iloc[0]["Dose"])
            if st.button("🔄 Start Over"):
                st.session_state.step = 1
                st.rerun()
