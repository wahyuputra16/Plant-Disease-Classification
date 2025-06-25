# 🌿 Plant Disease Classification with Deep Learning

This project is a web-based system that uses deep learning to automatically identify and classify plant diseases through leaf images. Built with Convolutional Neural Networks (CNN) and deployed via a Flask web app, it helps farmers and agricultural stakeholders detect diseases quickly and accurately.

---

## 🧠 Project Overview

- **Goal:** Automatically classify leaf images into 3 categories:
  - `Healthy`
  - `Powdery`
  - `Rust`
- **Model:** Trained using a Convolutional Neural Network (CNN)
- **Dataset Source:** [Kaggle Plant Disease Recognition Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset)
- **Frameworks:**
  - TensorFlow / Keras
  - Flask for web deployment

---

## 🚀 Features

- Upload leaf images via web interface
- Real-time prediction using a pre-trained model (`plant_disease_model.h5`)
- Clear interface styled with `style.css`
- Supports drag-and-drop image upload and displays prediction results

---

## 📁 Project Structure

```
Uas_CV/
├── app.py                  # Flask web application
├── plant_disease_model.h5 # Trained CNN model
├── static/
│   ├── style.css           # Web styling
│   └── uploads/            # Uploaded image storage
├── templates/
│   └── index.html          # HTML interface
└── .git/                   # Git metadata
```

---

## ⚙️ How to Run Locally

1. **Clone this repo:**
   ```bash
   git clone https://github.com/wahyuputra16/Plant-Disease-Classification.git
   cd Plant-Disease-Classification
   ```

2. **Install dependencies:**
   ```bash
   pip install flask tensorflow pillow
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📷 Sample Screenshot

> *(Insert a screenshot of the web interface here)*

---

## 📜 License

This project is for educational and research purposes only. Dataset belongs to the respective author on Kaggle.

---

## ✨ Credits

- Deep learning model inspired by plant pathology studies
- UI built with HTML/CSS
- Dataset: [Kaggle Plant Disease Recognition](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset)