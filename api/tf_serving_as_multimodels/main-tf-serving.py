

from fastapi import FastAPI, File, UploadFile,Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import sys
import asyncio
import requests

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def select_model(plant):
    if plant=='Potato':
        endpoint = "http://localhost:8501/v1/models/potato/labels/stable:predict"
        class_name= ["Early Blight", "Late Blight", "Healthy"]
    elif plant == 'Tomato':
        endpoint = "http://localhost:8501/v1/models/tomato/labels/stable:predict"
        class_name= ['Bacterial spot',
                     'Early blight',
                     'Late blight',
                     'Leaf Mold',
                     'Septoria leaf spot',
                     'Spider mites (Two spotted spider mite)',
                     'Target Spot',
                     'Tomato YellowLeaf Curl Virus',
                     'Tomato mosaic virus',
                     'Healthy']

    elif plant=='Pepper':
        endpoint = "http://localhost:8501/v1/models/pepper/labels/stable:predict"
        class_name= ['Bacterial Spot', 'Healthy']

    else:
        endpoint = "http://localhost:8501/v1/models/potato/labels/stable:predict"
        class_name= ["Early Blight", "Late Blight", "Healthy"]

    return endpoint,class_name

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),plant:str=Form(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    endpoint,class_name=select_model(plant)

    json_data = {
        "instances": img_batch.tolist()
    }

    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])

    predicted_class = class_name[np.argmax(prediction)]
    confidence = np.max(prediction)
    print(response.json())
    return {
        "class": predicted_class,
        "confidence": int(confidence*100)
    }

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    uvicorn.run(app, host='localhost', port=8000)