from sklearn.datasets import load_iris
from typing import Union
from fastapi import FastAPI, Body
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Load the Iris dataset
iris = load_iris()

# Load the model
filename = 'iris_model.joblib'
loaded_model = joblib.load(filename)

class IrisData(BaseModel):
    sepal_length: float = Body(..., gt=0, description="Length of sepal in cm")
    sepal_width: float = Body(..., gt=0, description="Width of sepal in cm")
    petal_length: float = Body(..., gt=0, description="Length of petal in cm")
    petal_width: float = Body(..., gt=0, description="Width of petal in cm")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict-iris")
def predit_iris(data: IrisData):
    new_data = np.array([
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width], # input1
    ])
    predictions = loaded_model.predict(new_data)
    predicted_species = iris.target_names[predictions[0]]

    return { "prediction": predicted_species }
