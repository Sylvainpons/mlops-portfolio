import joblib
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware  # Ajout de l'import manquant
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (à restreindre en production)
    allow_credentials=True,
    allow_methods=["POST"],  # Autoriser toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

model = joblib.load('best_iris_random_forest_model.pkl')

# Définir le format attendu pour la requête
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Route /predict
@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(data)
    species = ["setosa", "versicolor", "virginica"]
    return {"prediction": species[prediction[0]]}

# Lancer le serveur
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")