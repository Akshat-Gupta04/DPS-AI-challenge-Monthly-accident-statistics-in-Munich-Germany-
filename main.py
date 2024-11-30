import streamlit as st
import pickle
import pandas as pd

# Load the SARIMA model
with open("sarima_model_akshat.pkl", "rb") as file:
    model = pickle.load(file)

# Function to generate prediction
def generate_prediction(year, month):
    # Create a pandas `DatetimeIndex` for the input date
    start_date = pd.Timestamp(year=year, month=month, day=1)
    end_date = pd.Timestamp(year=year, month=month, day=1)
    
    # Generate prediction for the given date
    prediction = model.predict(start=start_date, end=end_date)
    return prediction.iloc[0]  # Extract the single predicted value

# Streamlit app
st.title("Digital Product School AI Challenge Entry")
st.write("Provide year and month to get the prediction.")

# Input fields for year and month
year = st.number_input("Year", min_value=2000, max_value=2100, value=2023, step=1)
month = st.number_input("Month", min_value=1, max_value=12, value=12, step=1)

# Predict button
if st.button("Get Prediction"):
    try:
        prediction = generate_prediction(year, month)
        
        # Prepare output in JSON format
        output = {
            "year": year,
            "month": month,
            "prediction": prediction
        }
        
        st.subheader("Prediction Output:")
        st.json(output)
    except Exception as e:
        st.error(f"Error: {e}")

# Add watermark text at the bottom
st.markdown(
    """
    <style>
        .watermark {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 12px;
            color: grey;
            opacity: 0.7;
        }
    </style>
    <div class="watermark">
        © 2024 Digital Product School - Built with ❤️ by Akshat Gupta: E22CSEU0059@bennett.edu.in
    </div>
    """,
    unsafe_allow_html=True
)
