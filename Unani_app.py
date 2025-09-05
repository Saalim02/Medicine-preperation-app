import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_excel("Y-Unani_medicines.xlsx")
df.columns = df.columns.str.strip()  # clean column names

st.title("🧑‍⚕️ Unani Medicine Doctor's Guide 🌿")

# --- Step 0: Doctor enters medicine name ---
medicine_name = st.text_input("Enter medicine name:")

if medicine_name:
    # Filter medicine by name (case insensitive)
    medicine = df[df["Medicine Name"].str.contains(medicine_name, case=False, na=False)]

    if medicine.empty:
        st.error("❌ Medicine not found. Please try another name.")
    else:
        # Initialize session state for steps
        if "step" not in st.session_state:
            st.session_state.step = 1

        # Step 1: Show Therapeutic uses
        if st.session_state.step == 1:
            st.subheader("🩺 Therapeutic Uses")
            st.write(medicine.iloc[0]["Therapeutic uses"])
            if st.button("Next ➡️"):
                st.session_state.step = 2
                st.rerun()

        # Step 2: Show Method of preparation
        elif st.session_state.step == 2:
            st.subheader("⚗️ Method of Preparation")
            st.write(medicine.iloc[0]["Method of preparation"])
            if st.button("Next ➡️"):
                st.session_state.step = 3
                st.rerun()

        # Step 3: Show Formulation composition
        elif st.session_state.step == 3:
            st.subheader("🧪 Formulation Composition")
            st.write(medicine.iloc[0]["Formulation composition"])
            if st.button("Next ➡️"):
                st.session_state.step = 4
                st.rerun()

        # Step 4: Show Dose
        elif st.session_state.step == 4:
            st.subheader("💊 Dose")
            st.write(medicine.iloc[0]["Dose"])
            if st.button("Next ➡️"):
                st.session_state.step = 5
                st.rerun()

        # Step 5: Show Mode of administration
        elif st.session_state.step == 5:
            st.subheader("💉 Mode of Administration")
            st.write(medicine.iloc[0]["Mode of administration"])
            if st.button("🔄 Start Over"):
                st.session_state.step = 1
                st.rerun()
