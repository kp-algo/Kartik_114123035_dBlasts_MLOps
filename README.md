# Cats and Dogs Image Classification - MLOps Project

This project uses machine learning to classify images as either cats or dogs. It includes a web application where users can upload an image to get predictions.

---

## Project Structure

- **`app.py`**: The main Python file that runs the web application.
- **`model.h5`**: The pre-trained model used for image classification.
- **`templates/`**: Contains the **index.html** for the web interface.

---

## Features

- A trained deep learning model for image classification.
- A simple web app interface for uploading images.
- Provides predictions instantly.

---

## Installation

### Prerequisites
1. Python 3.12.4 or later installed on your system.
2. Required libraries:
   - Flask
   - TensorFlow

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kp-algo/Kartik_114123035_dBlasts_MLOps
   ```
2. Navigate to the project directory:
   ```bash
   cd Kartik_114123035_dBlasts_MLOps
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Start the Flask web app:
   ```bash
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Upload an image (e.g., a picture of a cat or dog) and get the prediction.

---

## How It Works

1. **Model**: The `model.h5` file is a pre-trained deep learning model that predicts if an image is of a cat or dog. <br>
This model uses a Convolutional Neural Network (CNN) model built using the Keras Sequential API. Below is the screenshot of the summary of the model architecture:

![Screenshot of the summary of Model Architecture](https://github.com/kp-algo/Kartik_114123035_dBlasts_MLOps/blob/main/images/image.png?raw=true)

2. **Web App**: The `app.py` file serves as the backend, while the `templates/` folder contains the frontend files for the user interface.

---

## Demo

Here’s an example of the web interface:

![Screenshot of Web App](https://github.com/kp-algo/Kartik_114123035_dBlasts_MLOps/blob/main/images/Screenshot%202024-12-25%20213243.png?raw=true)

---

## Notes

This is my first project where I’m exploring MLOps. The setup might have some gaps, but I’ll update it as I learn more. Feedback is welcome!

---

## Credits

- Model trained using TensorFlow/Keras.
- Frontend designed with HTML, CSS, and JavaScript.
- Flask used to create the web app.

---

