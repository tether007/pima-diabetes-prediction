# 🩺 Pima Diabetes Prediction using Machine Learning

This repository contains an end-to-end Machine Learning project to predict the likelihood of diabetes in patients using the **Pima Indians Diabetes Dataset**.  
The project demonstrates data preprocessing, visualization, model building, and evaluation with multiple algorithms.

---

## 📊 Dataset
- **Source**: [Pima Indians Diabetes Database (Kaggle / UCI)](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Features**:  
  - Pregnancies  
  - Glucose  
  - BloodPressure  
  - SkinThickness  
  - Insulin  
  - BMI  
  - DiabetesPedigreeFunction  
  - Age  
- **Target**: Outcome (0 = Non-Diabetic, 1 = Diabetic)

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Handling missing values (KNN Imputer)
   - Feature scaling (MinMaxScaler)
   - Train-test split

2. **Exploratory Data Analysis (EDA)**
   - Histograms & Boxplots
   - Correlation Heatmap
   - Outcome distribution

3. **Model Building**
   - Logistic Regression (Baseline)
   - Decision Tree
   - Random Forest
   - Gradient Boosting & XGBoost

4. **Evaluation Metrics**
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC-AUC

---

## 📈 Results
- **Best Model**: Logistic Regression (Baseline)  
- **Why?** Outperformed more complex models on recall and F1-score, making it more reliable for healthcare use-case.

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/pima-diabetes-prediction.git
   cd pima-diabetes-prediction
