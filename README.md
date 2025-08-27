# 🧠 Multi-Class Classification using PyTorch

This repository showcases a complete pipeline for multi-class classification using PyTorch. It walks through data preprocessing, model architecture, training, evaluation, and visualization—all within a single, well-documented Jupyter notebook.

## 📌 Project Overview

The goal is to classify structured tabular data into multiple categories using a feedforward neural network. The notebook demonstrates how to build, train, and evaluate a model that generalizes well across unseen samples.

## 🚀 Technologies Used

- **PyTorch**: Deep learning framework for model definition and training
- **NumPy & Pandas**: Data manipulation and preprocessing
- **Scikit-learn**: Label encoding, train-test split, and evaluation metrics
- **Matplotlib & Seaborn**: Visualization of training performance and confusion matrix
- **Jupyter Notebook**: Interactive development and experimentation

## 🧠 Model Architecture

- **Input Layer**: Accepts numerical features from tabular data
- **Hidden Layers**: Two fully connected layers with ReLU activation
- **Output Layer**: Softmax activation for multi-class prediction
- **Loss Function**: `CrossEntropyLoss` for multi-class classification
- **Optimizer**: `Adam` with learning rate tuning

## 📊 Results

- ✅ **Validation Accuracy**: ~85%
- 📉 **Loss Curve**: Smooth convergence across training epochs
- 📈 **Confusion Matrix**: Strong class separation with minimal overlap
- 🔍 **Generalization**: Model performs well on unseen data

## 📁 Repository Contents

## 📁 Repository Structure

```text
├── pytorch_multiclass_classification.ipynb  # Main notebook with full pipeline  
├── requirement.txt                          # Python dependencies  
├── environment.yml                          # Conda environment setup  
├── checking_formate.py                      # Utility script for data format validation  
├── repairing_nootbook.py                    # Notebook repair script  
├── .gitignore                               # Git ignore rules  
```

## 🛠️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/arvind207kumar/Multi_Class_classification-using-PyTorch.git
   cd Multi_Class_classification-using-PyTorch
```
2. **Install dependencies**:
pip install -r requirement.txt
