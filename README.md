# Cloth-Recognition-Project

# 👕 Cloth Recognition Web Application — Jeans vs T-Shirt

A deep learning-based web application that classifies clothing images into Jeans or T-Shirt using a custom Convolutional Neural Network (CNN) built with TensorFlow/Keras.
The trained CNN model is integrated with a Flask web application, allowing users to upload a clothing image and receive the predicted class along with a confidence score through an interactive and modern web interface.

---

## 📌 Project Overview

The main objective of this project is to build an end-to-end image classification system using Deep Learning and Computer Vision.
In this project, a custom CNN model is trained on a clothing dataset containing two categories:

* 👖 Jeans
* 👕 T-Shirt

After training and evaluating the model, the trained CNN is saved as an `.h5` file and integrated into a Flask web application.
The Flask application provides a user-friendly interface where users can upload an image. The uploaded image is preprocessed and passed to the trained CNN model, which predicts whether the image belongs to the Jeans or T-Shirt category.

### Project Workflow
Dataset → Data Preprocessing → CNN Model Development → Model Training → Model Evaluation → Save Trained Model → Flask Integration → Image Upload → Image Preprocessing → CNN Prediction → Prediction + Confidence Score

####  🚀 Features
🧠 Custom CNN Model built using TensorFlow/Keras

👖 Jeans vs T-Shirt Classification
🌐 Flask Web Application
📤 Image Upload Functionality
🖼️ Dynamic Image Preview
📊 Prediction with Confidence Score
🎨 Modern Dark Glassmorphism UI
🔄 Smooth 3D Flip Animation
🧹 Clean TensorFlow/oneDNN Terminal Logs
⚡ Real-Time Image Prediction


### 🛠️ Tech Stack

* Technology        Purpose
* Python            Core Programming Language
* TensorFlow        Deep Learning Framework
* Keras             CNN Model Development
* Flask             Backend Web Framework
* OpenCV            Image Processing
* NumPy             Numerical Operations
* HTML5             Frontend Structure
* CSS3              Styling and Animations


### 🧠 CNN Model

The project uses a custom Convolutional Neural Network (CNN) for image classification.
The model is developed using TensorFlow/Keras and includes layers such as:

Conv2D
MaxPool2D
Flatten
Dense

### CNN Architecture

Input Image
     ↓
Convolutional Layer
     ↓
Max Pooling Layer
     ↓
Convolutional Layer
     ↓
Max Pooling Layer
     ↓
Flatten
     ↓
Dense Layer
     ↓
Output Layer (Jeans / T-Shirt)


### How CNN Works

The CNN automatically learns visual features from clothing images.
Conv2D layers extract important visual features such as edges, shapes, textures, and patterns.
MaxPooling layers reduce the spatial dimensions of feature maps while retaining important information.
Flatten layer converts the extracted feature maps into a one-dimensional vector.
Dense layers learn higher-level patterns from the extracted features.
Finally, the output layer generates the classification result.


### 📊 Dataset

The dataset contains images belonging to two clothing categories:

* Jeans

* T-Shirt

The dataset is used to train the CNN model to identify visual patterns associated with each clothing category.


### Dataset Structure

cloth_dataset/
│
├── Jeans/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
│└── T-Shirt/
│   ├── image1.jpg
│   ├── image2.jpg


### Image Preprocessing

Before images are passed to the CNN model, they are preprocessed using OpenCV and NumPy. The preprocessing pipeline includes:

Loading the image
Resizing the image
Converting the image into a suitable format
Normalizing pixel values
Converting the image into a NumPy array
Passing the processed image to the trained CNN model

### ⚙️ Model Training

The model training process follows a standard Deep Learning workflow:

Data Preparation: The dataset is organized into separate directories based on the class labels.
Data Preprocessing: Images are resized and normalized before being used for training.
CNN Model Creation: A custom CNN architecture is created using TensorFlow/Keras.
Model Training: The CNN model is trained on the prepared clothing dataset for multiple epochs to learn visual characteristics.
Model Evaluation: The trained model is evaluated using validation/test data to measure its classification performance.
Model Saving: After training, the model is saved as cloth_recognization_model.h5 for later use in the Flask application.

### 🌐 Flask Web Application

The trained CNN model is integrated with Flask to create a web-based prediction system. The Flask backend handles:

Loading the trained CNN model
Receiving uploaded images
Saving uploaded images temporarily
Image preprocessing
Making predictions and generating confidence scores
Sending results to the frontend

### 🖥️ Web Interface

The application provides a modern and interactive user interface with a dark glassmorphism design. Users can upload a clothing image, preview it, and view the predicted category along with the confidence score.
Example Predictions
Prediction: T-Shirt | Confidence: 94.32%
Prediction: Jeans | Confidence: 91.76%
(Note: The confidence score represents the model's output confidence and does not guarantee that the prediction is correct.)

### 📂 Project Structure

Cloth-Recognition-Project/
│
├── cloth_dataset/
│   ├── Jeans/
│   └── T-Shirt/
│
├── templates/
│   └── index.html
│
├── uploads/
│   └── # Uploaded images
│
├── app.py
├── cloth_recognization_model.h5
├── requirements.txt
└── README.md

### 🔍 How to Use
1. Run the Flask application (python app.py).
2. Open the application URL in your browser.
3. Upload an image of a Jeans or T-Shirt.
4. Preview your selected image and click the prediction button.
5. The application will process the image and display the predicted class and confidence score instantly.

### 🎯 Project Objective
The primary objective of this project is to demonstrate how a Deep Learning image classification model can be integrated into a real-world web application, combining Deep Learning, Computer Vision, and Web Development into a complete end-to-end workflow.

### 🏆 Conclusion
The Cloth Recognition Web Application is a CNN-based image classification project that recognizes clothing images as either Jeans or T-Shirts. By combining a custom TensorFlow/Keras model with a Flask web interface, this project demonstrates practical knowledge across Python, Deep Learning, Computer Vision, and Full-Stack Web Development.

### 👨‍💻 Author

Rehan Alam

Cloth Recognition Web Application built with ❤️ using Python, TensorFlow, Keras, OpenCV, NumPy, and Flask.
