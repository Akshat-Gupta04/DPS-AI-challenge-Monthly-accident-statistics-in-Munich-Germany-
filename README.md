# Accident Prediction Using SARIMA Model

## Overview
This project is part of the **Digital Product School AI Challenge**, where the objective is to predict the number of alcohol-related accidents (**“Alkoholunfälle”**) in Munich for a specified year and month. Using the **Monatszahlen Verkehrsunfälle** dataset from the **München Open Data Portal**, we created a predictive model based on historical accident data.

The solution involves data preprocessing, building a time-series model using SARIMA, and deploying a Streamlit application that provides predictions via a web interface.

---

## Dataset
The dataset contains monthly traffic accident statistics in Munich, including:

- **Category**: Type of accident (e.g., “Alkoholunfälle” - alcohol-related accidents).
- **Accident Type**: Subcategories or total accidents (`insgesamt` means total).
- **Year**: The year of occurrence.
- **Month**: The month of occurrence.
- **Value**: Number of accidents for the specified category and type.

**Important Notes:**
- The dataset contains records until **2021**, but only data up to **2020** was used for training to ensure consistent predictions for unseen data.

**Dataset Source**: [Monatszahlen Verkehrsunfälle - München Open Data Portal]([https://www.opengov-muenchen.de](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7))

---

## Project Workflow

### 1. Data Preprocessing
- Removed data after **2020** to create a consistent dataset for training.
- Filtered records to focus on **“Alkoholunfälle”** and **“insgesamt”** accident types.
- Processed the data to create a monthly time-series format for model training.

### 2. Model Development
- Used the **SARIMA (Seasonal ARIMA)** model for time-series forecasting.
- Trained the model on historical accident data up to **2020**.
- Evaluated the model’s accuracy using metrics such as Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE).

### 3. Streamlit Application
- Built a Streamlit app that provides:
  - Input fields for **year** and **month**.
  - A prediction for the specified date.
  - Visualization of historical trends.
  - JSON response for easy API integration.

---

## Features
- **Forecasting**: Predicts the number of alcohol-related accidents for a given year and month.
- **Interactive Visualization**: Historical accident trends are visualized in the app.
- **API Integration**: The app accepts POST requests with JSON inputs and returns predictions in JSON format.

---

## Installation and Deployment

### Requirements
- Python 3.10+
- Libraries: Streamlit, pandas, numpy, scikit-learn, statsmodels, matplotlib, pickle, etc.

### Setup
1. Clone the repository.
2. Install dependencies using the provided `requirements.txt`.
3. Run the Streamlit app locally.
4. Deploy the app to a cloud service like Streamlit Cloud, Heroku, or AWS.

---

## Usage

### Web Application
- Access the Streamlit app, input the desired **year** and **month**, and get predictions along with historical accident trends.

### API
- Use the POST endpoint `/predict` to send a request with year and month as JSON and receive predictions in JSON format.

---

## Deployment Details
- **GitHub Repository**: [Repository]([https://github.com/Akshat-Gupta04/German_model](https://github.com/Akshat-Gupta04/DPS-AI-challenge-Monthly-accident-statistics-in-Munich-Germany-.git))
- **Deployed App URL**: [Streamlit App]([https://germanmodel.streamlit.app](https://germanmodel-s8qi2zaxwbqxgyfqddgssd.streamlit.app))
- **POST Endpoint**: `{Deployed App URL}/predict`

---

## Future Improvements
1. Extend the model to predict other accident categories.
2. Improve accuracy by exploring advanced models like LSTM or Prophet.
3. Add confidence intervals for predictions.

---

## Acknowledgments
- Dataset provided by **München Open Data Portal**.
- Challenge organized by **Digital Product School**.
- Submission created by **Akshat Gupta**.

Thank you for considering my submission!
