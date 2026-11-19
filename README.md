# Health Insurance Prediction

## Project Overview

This project uses machine learning to help health insurance agents discuss insurance plans with customers by providing an estimated insurance-related amount based on the customer's personal, health, and policy-related information.

The application is designed to support conversations about coverage, premium, and expected insurance costs by providing a data-driven estimate.

## Objective

The objective of this project is to build a machine learning model that can estimate the expected health insurance amount for an individual based on relevant customer information.

The prediction can help an insurance agent:

- Discuss suitable coverage options with customers
- Explain estimated insurance costs
- Support premium-related discussions
- Provide a data-driven estimate during customer interactions

## Dataset

The dataset contains personal, health, and insurance-related information about individuals.

The target variable is:

- `claim` — predicted insurance claim amount

> The dataset is not included in this repository.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Workflow

1. Data collection
2. Data cleaning
3. Missing-value handling
4. Exploratory Data Analysis
5. Feature selection
6. Categorical feature encoding
7. Train-test split
8. Feature preprocessing
9. Model training
10. Hyperparameter tuning
11. Model evaluation
12. Prediction through Streamlit

## Model

A **Random Forest Regressor** is used to predict the insurance amount.

The trained model is saved using Joblib and loaded by the Streamlit application to generate predictions.

## Features Used

The model uses relevant customer information such as:

- Age
- Sex
- BMI
- Hereditary diseases
- Smoking status
- City
- Blood pressure
- Diabetes
- Regular exercise
- Job title

## Data Leakage Prevention

Features that could provide information only after a medical treatment or hospitalization were excluded from the model.

Examples include:

- Hospital bill amount
- Length of stay
- ICU days
- Hospital name
- Room category
- Claim date
- Other post-treatment information

This helps ensure that the model does not use information that would only become available after the event being predicted.

## Streamlit Application

The project includes a Streamlit application in `app1.py`.

To run the application:

```bash
streamlit run app1.py
```

## Project Structure

```text
Health-Insurance-Prediction/
│
├── app1.py
├── health_insurance_analysis.ipynb
├── random_forest.pkl
├── screenshot_image.jpg
├── README.md
└── .gitignore
```



