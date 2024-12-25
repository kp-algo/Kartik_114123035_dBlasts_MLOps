# Cats and Dogs Image Classification - MLOps Project

This project uses machine learning to classify images as either cats or dogs. It includes a web application where users can upload an image to get predictions.

---

## Project Structure

- **`app.py`**: The main Python file that runs the web application.
- **`model.h5`**: The pre-trained model used for image classification.
- **`templates/`**: Contains the HTML, CSS, and JavaScript files for the web interface.

---

## Features

- A trained deep learning model for image classification.
- A simple web app interface for uploading images.
- Provides predictions instantly.

---

## Installation

### Prerequisites
1. Python 3.7 or later installed on your system.
2. Required libraries:
   - Flask
   - TensorFlow
   - Any other libraries (add as necessary).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cats-dogs-mlops.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cats-dogs-mlops
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

1. **Model**: The `model.h5` file is a pre-trained deep learning model that predicts if an image is of a cat or dog.
2. **Web App**: The `app.py` file serves as the backend, while the `templates/` folder contains the frontend files for the user interface.

---

## Demo

Here’s an example of the web interface:

![Screenshot of Web App](https://github.com/kp-algo/Kartik_114123035_dBlasts_MLOps/raw/c3e7d4b18591144a11ac648b24b154ec2af584a4/images/Screenshot%202024-12-25%20213243.png
)

---

## Notes

This is my first project where I’m exploring MLOps. The setup might have some gaps, but I’ll update it as I learn more. Feedback is welcome!

---

## Credits

- Model trained using TensorFlow/Keras.
- Frontend designed with HTML, CSS, and JavaScript.
- Flask used to create the web app.

---

## License

This project is licensed under the MIT License.
