from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import uuid

app = Flask(__name__)
model = tf.keras.models.load_model("plant_disease_model.h5")

class_names = ["Healthy", "Powdery", "Rust"]

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def preprocess_image(image):
    image = image.resize((64, 64))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            filename = f"{uuid.uuid4().hex}.png"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            img = Image.open(filepath).convert("RGB")
            input_image = preprocess_image(img)
            preds = model.predict(input_image)
            prediction = class_names[np.argmax(preds)]

    return render_template("index.html", prediction=prediction, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
