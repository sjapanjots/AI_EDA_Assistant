# 🐶🐱 Dog vs Cat Image Classifier using Deep Learning

A convolutional neural network (CNN)-based deep learning model that classifies images of dogs and cats using TensorFlow and Keras.

---

## 🚀 Project Overview

This project demonstrates a simple deep learning workflow using a Convolutional Neural Network (CNN) to distinguish between dog and cat images. It includes data preprocessing, model building, training, evaluation, and prediction on custom inputs.

---

## 💻 Tech Stack

- **Python**
- **TensorFlow / Keras** – For building and training the CNN
- **OpenCV** – For image loading and preprocessing
- **NumPy / Matplotlib** – For array handling and visualization
- **Jupyter Notebook** – For development and experimentation

---

## 📄 What's Inside

- `Dog_vs_Cat_CNN.ipynb`  
  Jupyter Notebook containing the full code for:
  - Loading and preprocessing image data
  - Creating and training the CNN model
  - Evaluating accuracy and loss
  - Making predictions on test data

- `dataset/`  
  Contains training and test images of dogs and cats, typically structured as:
  ```
  dataset/
    └── train/
        ├── cats/
        └── dogs/
    └── test/
  ```

---

## 🧠 How It Works

1. **Data Preparation**  
   Images are resized and normalized. They are labeled automatically based on directory structure (`cats/` or `dogs/`).

2. **Model Architecture**  
   A basic CNN with convolutional, max-pooling, and dense layers. Compiled with `binary_crossentropy` loss for binary classification.

3. **Training**  
   Model is trained over multiple epochs, with accuracy and loss visualized using plots.

4. **Prediction**  
   Custom images can be passed through the model to predict if it's a **dog** or a **cat**.

---

## 📦 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sjapanjots/Dog_Vs_Cat_Deep_Learning.git
   cd Dog_Vs_Cat_Deep_Learning
   ```

2. **Install required packages**:
   ```bash
   pip install tensorflow opencv-python matplotlib numpy jupyter
   ```

3. **Launch the notebook**:
   ```bash
   jupyter notebook
   ```

4. Open `Dog_vs_Cat_CNN.ipynb` and run all cells.

---

## 🖼️ Sample Result

- Input: Random image of a dog  
- Output: **Predicted: Dog**

- Input: Random image of a cat  
- Output: **Predicted: Cat**

---

## 🙋‍♂️ Author

**Japanjot Singh**  
Data Scientist & ML Enthusiast  
📬 sjapanjots@gmail.com