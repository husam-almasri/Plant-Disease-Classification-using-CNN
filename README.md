# Plant Disease Classification using CNN:

## Table of Content
  * [Overview](#overview)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Future scope](#future-scope)


### Website screenshot:
![](/images/screencapture-homepage.png)

### Screenshot of the results:
![](/images/screencapture-results.png)

## Overview
This is an end-to-end deep learning project in the agriculture domain. Farmers every year face economic loss and crop waste due to various diseases in plants. I will use image classification using CNN and built a testpad website using which a farmer can take a picture and the website will tell him if the plant has a disease or not.

Dataset from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village). This dataset has data about three types of vegetables (Potato, Tomato, and Pepper), each kind has images of healthy and different types of diseases related to its kind. 

We will first Load data into tf.Dataset. I used split_folders library to split datasets into THREE main folders, each has one type of vegetable (Potato, Tomato, and Pepper).

The second step is building and training 3 CNN models, each is trained on one type of vegetable (Potato, Tomato, and Pepper) by Sklearn, TensorFlow, and Keras using two ways for augmentation:

1- Explicit data augmentation layer to train the models.

2- ImageDataGenerator API, which allows you to load the images from the disk and augment them in simple 2 line code.

Then Make predictions/inferences on sample images and export the model to a file on disk.
The goal of these models would be to classify these images as either healthy or not and specify, if not healthy, which kind of disease they have.

Thirdly, tf serving and FastAPI:
tf serving is a tool that allows you to bring up a model server with a single command. It also allows doing model version management, loading of models dynamically. It supports features such as version labels, configurable version policy, etc.
In this project, I will let the tf serving handle the 3 models, each prepared for more versions in the future, and leave FastAPI to handle the image processing and use the load the saved model from tf serving to serve HTTP requests. 

The fourth component is the website built in HTML5, CSS3, and JavaScript that allows the user to select which kind of vegetable he wants to check and add a leaf image for the selected plant. The website will call python FastAPI server which, in turn, calls the related model from tf serving to perform the inference.

![](/images/Workflow-chart.png)

Technology and tools used in this project:
- Python
- Numpy and Pandas for data cleaning
- Matplotlib for data visualization
- Sklearn for model building
- Jupyter notebook, Visual Studio code, and pycharm as IDE
- Tensorflow, Keras, CNN, data augmentation, and tf dataset for Models Building
- Docker, tensorflow serving, and FastAPI for Backend Server and ML Ops.
- Postman application for tf serving and FastAPI web server testing.
- HTML5, CSS3, and JavaScript for Frontend


## Installation
The Code is written in Python 3.9.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

```
bash
pip install -r requirements.txt
```

### Running the API

#### Using FastAPI

1. Get inside `api` folder

```
bash
cd api
```

2. Run the FastAPI Server using uvicorn

```
bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8000`

#### Using FastAPI & TF Serve

1. Get inside `api/tf_serving_as_multimodels` folder

```
bash
cd api/tf_serving_as_multimodels
```

2. Update the paths in `models.config` file.
3. Run the TF Serve (Update config file path below)

```
bash
docker run -t --rm -p 8501:8501 -v C:/projects/plant_disease_classification/plant_disease_classification/:/plant_disease_clf tensorflow/serving --rest_api_port=8501 --allow_version_labels_for_unavailable_models=true --model_config_file=plant_disease_clf/api/tf_serving_as_multimodels/models.config
```

4. Run the FastAPI Server using uvicorn
   For this you can directly run it from your main.py or main-tf-serving.py using pycharm run option, OR you can run it from command prompt as shown below,

```
bash
uvicorn main-tf-serving:app --reload --host 0.0.0.0
```

5. Your API is now running at `0.0.0.0:8000`


## Directory Tree

```
| README.md
| api
| | requirements.txt
| +---fastapi
| | main.py
| +---tf_serving_as_multimodels
| | docker command.txt
| | main-tf-serving.py
| | models.config
| frontend
| | index.html
| | main.css
| | main.js
| | main_img.jpg
| | pepper_img.jpg
| | Potato_img.jpg
| | tomato_img.jpg
| images
| | screencapture-homepage.png
| | creencapture-results.png
| | workflow-chart.png
|  training
| | PDC.ipynb
| | PDC_ImageDataGenerator.ipynb
|  saved_models
| +---fastapi
| | +---pepper_PDC_ImageDataGenerator
| | +---potato_PDC_ImageDataGenerator
| | \---tomato_PDC_ImageDataGenerator
| \---tf-serving
|   +---models
|   | +---pepper_PDC_ImageDataGenerator
|   | +---potato_PDC_ImageDataGenerator
|   | \---tomato_PDC_ImageDataGenerator
``` 

## Future scope

* Add more types of vegetables and fruits.
* Model Optimization: Quantization, Tensorflow lite
* Frontend: React JS, React Native
