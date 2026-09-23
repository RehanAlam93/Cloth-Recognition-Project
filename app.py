import os
# Hide TensorFlow and Abseil warnings from the terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Define model path and target image size for preprocessing
MODEL_PATH = r'EDA\cloth_recognization_model.h5'
IMG_SIZE = 128

# Load the trained CNN model quietly
if os.path.exists(MODEL_PATH):
  model = load_model(MODEL_PATH, compile=False)


@app.route('/')
def home():
  """Renders the main upload page."""
  return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
  """Handles image upload, preprocesses the input, and returns the model prediction

  with confidence score.
  """
  if 'file' not in request.files:
    return render_template(
        'index.html', prediction='Please upload an image file.'
    )

  file = request.files['file']
  if file.filename == '':
    return render_template('index.html', prediction='No selected file.')

  if file:
    # Save the uploaded file temporarily
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, file.filename)
    file.save(filepath)

    try:
      # Preprocess the uploaded image
      img = image.load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
      img_array = image.img_to_array(img) / 255.0
      img_array = np.expand_dims(img_array, axis=0)

      # Perform prediction
      prediction_prob = model.predict(img_array)[0][0]

      # Map prediction probability to class labels
      if prediction_prob > 0.5:
        result = 'T-Shirt'
        confidence = round(float(prediction_prob) * 100, 2)
      else:
        result = 'Jeans'
        confidence = round(float(1 - prediction_prob) * 100, 2)

      return render_template(
          'index.html', prediction=result, confidence=confidence
      )

    except Exception as e:
      return render_template(
          'index.html', prediction=f'An error occurred during prediction: {e}'
      )


if __name__ == '__main__':
  app.run(debug=True)