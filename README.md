# MNIST Classifier

Welcome to my first neural network project using TensorFlow and Keras to classify handwritten digits from the popular MNIST dataset. This is my first time experimenting with Neural Networks and Machine Learning in general. Hope you like it :>

---

## 📂 **Project Overview**

This repo contains two versions of my MNIST classification script:

1. **Basic Model (main.py)**

   - Standard fully connected neural network implemented using Keras' Layers.
   - Trains for fixed number of epochs (10).

2. **Callback Model (main-callback.py)**
   - Same architecture as the basic model.
   - Implements an **endtraining** callback to end training when **95% accuracy** is reached.
   - Uses less time for final accuracy results.

---

## 🏗️ **Model Architecture**

- Input: Flatten (28x28 images from the dataset)
- Dense(128, ReLU)
- Dense(64, ReLU)
- Dropout(0.2)
- Dense(10, softmax)

---

## ⚡ **Callback Concept**

The **callback version** uses Keras’ Callback to:

✅ Monitor training accuracy over epochs.  
✅ Stop training once **accuracy >= 95%**, saving time and avoiding overfitting.

---

## 📈 **Results**

| Version  | Test Accuracy           |
| -------- | ----------------------- |
| Basic    | ~99.06% after 10 epochs |
| Callback | ~97.33% ater 3 epochs   |

---

## **How to Run**

1. _Clone the repo :_
   git clone https://github.com/sreyanshacharya/mnist-classifier.git
   cd mnist-classifier

2. _Install dependencies :_
   pip install -r requirements.txt

3. _Run the Scripts :_
   (for the base version):
   python main.py

(for the callback version):
python main-callback.py

---

## 📝 **What I Learned**

- Functioning of basic neural networks.
- TensorFlow basics: datasets, models, layers.
- Model compilation and training.
- Datasets of Keras.
- Implementing callbacks for early stopping based on accuracy.

---

## 🔮 **Next Steps**

- Implement **CNN architecture** for higher accuracy.
- Use another included **Fashion MNIST** dataset.

---

### ✨ **Author**

**Sreyansh Acharya (bread)** – _CS Student and aspiring ML Engineer with interests in machine learning, neural networks and rock music. 🤘🏻_
**Connect With Me**
- sreyanshacharyaa@gmail.com
- github.com/sreyanshacharya

---
