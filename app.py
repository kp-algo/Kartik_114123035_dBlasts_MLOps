from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("model.h5")
model2 = tf.keras.models.load_model("kutta_billi.h5")


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/model_1', methods=['POST', 'GET'])
def predict_result():
        if request.method == "POST":
        # Retrieve the uploaded image
            file = request.files['img_file']

        # Process the image
            img = Image.open(file.stream).convert('RGB') 
            img = img.resize((256, 256)) 
            img_arr = np.array(img) / 255.0  
            img_arr = np.expand_dims(img_arr, axis=0)  

        # Make prediction
            prediction = model.predict(img_arr)[0][0]  
            result = 'Dog' if prediction > 0.5 else 'Cat'

            return jsonify({'prediction': result})

@app.route('/model_2', methods = ['POST'])
def model_2():
    if request.method == "POST":
        file = request.files['img_file']
        img = Image.open(file.stream).convert('RGB')
        img = img.resize((128,128))
        img_arr = np.array(img)/255.0
        img_arr = np.expand_dims(img_arr, axis =0)

        prediction = model2.predict(img_arr)[0][0]
        result = 'Dog' if prediction > 0.5 else 'Cat'

        return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, port=2000)


