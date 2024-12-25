from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("model.h5")

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_result():
    if request.method == 'POST':
        # Retrieve the uploaded image
        file = request.files['image']

        # Process the image
        img = Image.open(file.stream).convert('RGB')  # Convert to RGB to handle all formats
        img = img.resize((256, 256))  # Resize to the model's input size
        img_arr = np.array(img) / 255.0  # Normalize pixel values
        img_arr = np.expand_dims(img_arr, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(img_arr)[0][0]  # Get the first (and only) prediction
        result = 'Dog' if prediction > 0.5 else 'Cat'

        return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
