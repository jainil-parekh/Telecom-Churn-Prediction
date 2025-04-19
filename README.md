# Telco Customer Churn Prediction 📉📈

This project applies machine learning to predict whether a telecom customer is likely to churn, based on demographic, service usage, and billing data. It's designed to showcase skills in ML modeling, data preprocessing, evaluation, and model deployment readiness.

---

## 🚀 Key Features

✅ Trained and compared multiple ML models:  
&nbsp;&nbsp;&nbsp;&nbsp;• Random Forest, Logistic Regression, XGBoost, LightGBM  
✅ Evaluated models using:  
&nbsp;&nbsp;&nbsp;&nbsp;• Accuracy, Precision, Recall, F1-Score, ROC-AUC  
✅ Visualized:  
&nbsp;&nbsp;&nbsp;&nbsp;• ROC curves and feature importances  
✅ Built a reusable data preprocessing pipeline  
✅ Saved the best-performing model using `joblib` for deployment

---

## 📊 Tools & Technologies

- Python, Pandas, NumPy
- Scikit-learn, XGBoost, LightGBM
- Matplotlib, Seaborn
- joblib (for model serialization)

---

## ✅ Results

- Best Model: **XGBoost Classifier**
- Accuracy: **81.34%**
- ROC-AUC Score: **0.84**
- Precision: **0.82**
- Recall: **0.81**
- F1-Score: **0.81**

## 📦 Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/telco-customer-churn.git
cd telco-customer-churn

2. **Create a Virtual Environment (Recommended)**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Notebook

jupyter notebook notebooks/telco_churn_analysis.ipynb

5. To load the trained model and make predictions:

import joblib
model = joblib.load('models/telco_churn_model.pkl')




```
