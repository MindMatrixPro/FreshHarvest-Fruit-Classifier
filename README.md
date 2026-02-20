<h2 align="center">FreshHarvest Fruit Freshness Detection: AI-Powered Quality Control</h2>
<h2 align="center">🍓🥭🍉🍏🍍🍇</h2>

<p align="center"><b>Automating fruit freshness inspection using deep learning and a business-friendly demo app</b></p>

<p align="center">
  <a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/🍉%20Streamlit-1.45.0-ff4b4b?logo=streamlit&logoColor=white"></a>
  <a href="https://pytorch.org/"><img alt="PyTorch" src="https://img.shields.io/badge/🍍%20PyTorch-2.7.1-ee4c2c?logo=pytorch&logoColor=white"></a>
  <a href="https://pandas.pydata.org/"><img alt="Pandas" src="https://img.shields.io/badge/🍏%20Pandas-2.2.3-150458?logo=pandas&logoColor=white"></a>
  <a href="https://scikit-learn.org/"><img alt="Scikit-Learn" src="https://img.shields.io/badge/🍇%20Scikit--Learn-1.7.1-f7931e?logo=scikit-learn&logoColor=white"></a>
</p>

---

## Overview

**FreshHarvest Logistics** is a leading cold warehouse provider in California, sourcing select locally grown fruits from nearby farmers and delivering them to premium supermarkets. Their high-end clientele demands *near-perfect freshness*, with a service level where even **one defective fruit per thousand is unacceptable**.

To meet this standard, we developed an **AI-powered freshness inspection system** using **Convolutional Neural Networks (CNNs)** and **Transfer Learning**. The system detects overripe or spoiled fruits from conveyor belt images and alerts manual checkers, reducing human error and improving efficiency.

---

## Key Features

- **CNN-Based Quality Control**: Detects fresh vs. spoiled fruits across 8 categories.
- **Two-Phase Model Training**:  
  1. Baseline CNN model (no transfer learning, no regularization)  
  2. Optimized ResNet50 transfer learning model with regularization & hyperparameter tuning  
- **Real-Time Demo App**: Interactive Streamlit app with drag-and-drop image classification.
- **End-to-End Pipeline**:
  - Data ingestion & augmentation
  - Dataset splitting (train/val/test)
  - Model training, optimization, and saving
  - Deployment-ready prediction API
- **Supports 8 Fruits**: Banana, Lemon, Lulo, Mango, Orange, Strawberry, Tamarillo, Tomato — each classified as *Fresh* or *Spoiled*.

---

## 🚀 Launch App
[https://freshharvest-fruit-classifier.streamlit.app/](https://freshharvest-fruit-classifier.streamlit.app/)

![app](Project%20Screenshot%201.JPG)


### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tiknaavenger/FreshHarvest-Fruit-Classifier.git
   cd FreshHarvest-Fruit-Classifier
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

## Contributing

To Contribute, please submit issues or pull requests for enhancements or fixes.

---

## License

Licensed under the Apache 2.0 License.

---
