import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved Random Forest model
model = joblib.load("rf_autism_model.pkl")

st.set_page_config(page_title="Autism Gene Predictor", layout="wide")
st.title("🧬 Autism Genetic Score Prediction App")
st.write("Provide gene-related details to predict if it’s Syndromic or Non-Syndromic")

# Sample encoded values (should match your label encoders used during training)
gene_symbol_options = list(range(0, 50))         # Replace with actual label encoded value ranges
gene_name_options = list(range(0, 50))           # Replace with actual label encoded value ranges
ensembl_id_options = list(range(0, 50))          # Replace with actual label encoded value ranges
chromosome_options = list(range(0, 25))          # Replace with actual label encoded value ranges
genetic_category_options = list(range(0, 5))     # Replace with actual label encoded value ranges

# User input form
status = st.selectbox("Gene Status", options=[0, 1])
gene_symbol = st.selectbox("Gene Symbol (encoded)", gene_symbol_options)
gene_name = st.selectbox("Gene Name (encoded)", gene_name_options)
ensembl_id = st.selectbox("Ensembl ID (encoded)", ensembl_id_options)
chromosome = st.selectbox("Chromosome (encoded)", chromosome_options)
genetic_category = st.selectbox("Genetic Category (encoded)", genetic_category_options)
gene_score = st.slider("Gene Score", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
number_of_reports = st.number_input("Number of Reports", min_value=0, value=1)

# Prepare input for prediction
input_data = pd.DataFrame([[
    status, gene_symbol, gene_name, ensembl_id,
    chromosome, genetic_category, gene_score, number_of_reports
]], columns=['status', 'gene-symbol', 'gene-name', 'ensembl-id',
             'chromosome', 'genetic-category', 'gene-score', 'number-of-reports'])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "🟢 Syndromic (1)" if round(prediction) == 1 else "🔵 Non-Syndromic (0)"
    st.success(f"**Prediction:** {result}")






