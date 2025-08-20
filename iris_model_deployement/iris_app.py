import streamlit as st
import requests

st.title("🌸 Iris Flower Prediction API")

st.markdown("""
Enter the features of the iris flower and click **Predict** to see the predicted species.
""")

# Inputs interactifs
sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.1, step=0.1)
sepal_width  = st.slider("Sepal Width (cm)", min_value=2.0, max_value=5.0, value=3.5, step=0.1)
petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=1.4, step=0.1)
petal_width  = st.slider("Petal Width (cm)", min_value=0.1, max_value=3.0, value=0.2, step=0.1)

# Bouton pour prédiction
if st.button("Predict"):
    url = "http://localhost:8000/predict"  # Ton API FastAPI
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Prediction: **{prediction}**")
    else:
        st.error("Error contacting the API. Make sure FastAPI server is running.")
