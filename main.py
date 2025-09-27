import streamlit as st
import pandas as pd
import joblib
import os

# ================================
# Load Model Safely
# ================================
MODEL_PATH = r"model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found at: {MODEL_PATH}")
    st.stop()

try:
    clf = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ================================
# Streamlit Page Setup
# ================================
st.set_page_config(page_title="Trading Classification Dashboard", layout="wide")

# ================================
# Header
# ================================
st.markdown(
    """
    <h1 style="text-align:center; color:#fff;">
        Trading Classification Dashboard
    </h1>
    <p style="text-align:center; font-size:18px; color:#fff;">
        Enter trade details below and get predictions from your trained ML model
    </p>
    <hr style="border:1px solid #ccc;">
    """,
    unsafe_allow_html=True
)

# ================================
# Input Section
# ================================
st.subheader("Input Features")

tabs = st.tabs(["Numeric Features", "Categorical Features"])

with tabs[0]:
    col1, col2, col3 = st.columns(3)
    with col1:
        execution_price = st.number_input("Execution Price", min_value=0.0, step=0.01)
        closed_pnl = st.number_input("Closed PnL", step=0.01)
    with col2:
        size_tokens = st.number_input("Size Tokens", min_value=0.0, step=0.01)
        fee = st.number_input("Fee", step=0.01)
    with col3:
        size_usd = st.number_input("Size USD", min_value=0.0, step=0.01)
        value = st.number_input("Value", step=0.01)

with tabs[1]:
    col4, col5, col6 = st.columns(3)
    with col4:
        account = st.text_input("Account")
        side = st.selectbox("Side", ["Buy", "Sell"])
    with col5:
        coin = st.text_input("Coin")
        start_position = st.selectbox("Start Position", ["Long", "Short"])
    with col6:
        direction = st.selectbox("Direction", ["Up", "Down"])
        crossed = st.selectbox("Crossed", ["Yes", "No"])

# ================================
# Prepare Data
# ================================
input_data = {
    "Execution Price": execution_price,
    "Size Tokens": size_tokens,
    "Size USD": size_usd,
    "Closed PnL": closed_pnl,
    "Fee": fee,
    "value": value,
    "Account": account,
    "Coin": coin,
    "Side": side,
    "Start Position": start_position,
    "Direction": direction,
    "Crossed": crossed,
}
input_df = pd.DataFrame([input_data])

# ================================
# Prediction Section
# ================================
st.subheader("Prediction")

predict_button = st.button("Run Prediction", use_container_width=True)

if predict_button:
    try:
        prediction = clf.predict(input_df)[0]

        st.markdown(
            f"""
            <div style="padding:20px; border-radius:15px; background-color:#D5F5E3; text-align:center;">
                <h2 style="color:#1E8449;">Model Prediction</h2>
                <p style="font-size:22px; font-weight:bold; color:#145A32;">
                    {prediction}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("View Input Data"):
            st.dataframe(input_df, use_container_width=True)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
else:
    st.info("Enter details above and click **Run Prediction**")
