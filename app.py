import streamlit as st
import pandas as pd
import numpy as np
import re
import os

# --- EMAIL CONFIGURATION (DISABLED FOR NOW) ---
# We will simulate sending the email in this version.
SENDER_EMAIL = "test@example.com" 

def validate_email(email):
    """Checks if the email format is valid."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def calculate_topsis(df, weights, impacts):
    """Performs the TOPSIS calculation logic."""
    try:
        # Prepare data (drop the first column which is usually Name/ID)
        # We assume the first column is non-numeric (Fund Name)
        data = df.iloc[:, 1:].values.astype(float)
        
        # Normalize
        rss = np.sqrt(np.sum(data**2, axis=0))
        if (rss == 0).any():
             return None, "Error: Standard deviation of a column is zero."
             
        normalized_data = data / rss

        # Apply Weights
        weighted_data = normalized_data * weights

        # Ideal Best and Worst
        ideal_best = []
        ideal_worst = []

        for i in range(len(weights)):
            if impacts[i] == '+':
                ideal_best.append(np.max(weighted_data[:, i]))
                ideal_worst.append(np.min(weighted_data[:, i]))
            else:
                ideal_best.append(np.min(weighted_data[:, i]))
                ideal_worst.append(np.max(weighted_data[:, i]))

        ideal_best = np.array(ideal_best)
        ideal_worst = np.array(ideal_worst)

        # Euclidean Distances
        s_plus = np.sqrt(np.sum((weighted_data - ideal_best)**2, axis=1))
        s_minus = np.sqrt(np.sum((weighted_data - ideal_worst)**2, axis=1))

        # Performance Score
        total_dist = s_plus + s_minus
        score = np.divide(s_minus, total_dist, out=np.zeros_like(s_minus), where=total_dist!=0)

        # Append to original DF
        df['Topsis Score'] = score
        df['Rank'] = df['Topsis Score'].rank(ascending=False, method='min').astype(int)

        return df, None

    except Exception as e:
        return None, str(e)

# --- STREAMLIT UI ---
st.set_page_config(page_title="TOPSIS Web Service", page_icon="📊")

st.title("📊 TOPSIS Web Service")
st.markdown("Upload your data, set parameters, and receive the ranked results via email.")

# 1. Inputs
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])
weights_input = st.text_input("Weights (comma separated)", value="1,1,1,1,1")
impacts_input = st.text_input("Impacts (comma separated, + or -)", value="+,+,-,+,+")
email_input = st.text_input("Email ID (to receive results)", value="user@example.com")

# 2. Submit Button
if st.button("Submit"):
    # --- VALIDATIONS ---
    if not uploaded_file:
        st.error("Please upload an input file.")
        st.stop()
        
    if not weights_input or not impacts_input or not email_input:
        st.error("All fields are required.")
        st.stop()

    if not validate_email(email_input):
        st.error("Invalid Email ID format.")
        st.stop()

    # Read File
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Check Columns (Must be >= 3)
    if df.shape[1] < 3:
        st.error("Input file must contain three or more columns.")
        st.stop()

    # Check Numeric Values (From 2nd column onwards)
    try:
        test_df = df.iloc[:, 1:].astype(float)
    except ValueError:
        st.error("From 2nd to last columns must contain numeric values only.")
        st.stop()

    # Parse Weights and Impacts
    try:
        weights = [float(w) for w in weights_input.split(',')]
    except ValueError:
        st.error("Weights must be numeric values separated by commas.")
        st.stop()

    impacts = impacts_input.split(',')
    if not all(i in ['+', '-'] for i in impacts):
        st.error("Impacts must be either '+' or '-'.")
        st.stop()

    # Check Parameter Lengths
    num_cols = df.shape[1] - 1  # Exclude first column
    if len(weights) != num_cols or len(impacts) != num_cols:
        st.error(f"Count mismatch! Columns: {num_cols}, Weights: {len(weights)}, Impacts: {len(impacts)}.")
        st.stop()

    # --- PROCESSING ---
    with st.spinner('Calculating TOPSIS Score...'):
        result_df, error_msg = calculate_topsis(df.copy(), weights, impacts)

        if error_msg:
            st.error(error_msg)
        else:
            # --- SIMULATE EMAIL SENDING ---
            with st.spinner(f'Sending result to {email_input}...'):
                import time
                time.sleep(1) # Fake delay to look real
                
                # Success message (Simulated)
                st.success(f"Success!Result file 'sent' to {email_input}")
                st.balloons()
                
                # Show result on screen since we didn't actually email it
                st.write("### Result Preview")
                st.dataframe(result_df)
                
                # Allow download directly (optional, since email is disabled)
                csv = result_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Result CSV",
                    data=csv,
                    file_name='topsis_result.csv',
                    mime='text/csv',
                )