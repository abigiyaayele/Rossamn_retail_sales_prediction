# Rossmann Pharmaceuticals Sales Forecasting

## Overview

This project aims to build an end-to-end system for predicting daily sales in Rossmann Pharmaceuticals stores across several cities, six weeks ahead of time. The goal is to provide the finance team with accurate forecasts to help in better planning and decision-making. The solution involves both traditional machine learning and deep learning approaches, ensuring robust and scalable predictions.

## Table of Contents
- [Business Need](#business-need)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Approaches](#approaches)
- [Deliverables](#Deliverables)
  

## Business Need

The finance team at Rossmann Pharmaceuticals currently relies on store managers' experience and judgment to forecast sales. The need for a more systematic and data-driven approach is evident, as accurate sales predictions can significantly impact inventory management, staffing, and promotional strategies.


## Project Structure

```plaintext
Rossamn_retail_sales_prediction/
├── notebooks/
│   ├── EDA.ipynb  
│   ├── modeling.ipynb
│   ├── cleaning.ipynb
│   ├── Readme.md
│   └── ...
├── src/
│     ├── cleaning_raw_data.py
│     ├── main.py
│     └── ...
├── store_data_sql.py //database.py
├── Test/
│     ├── init.py
│     └── ...
├── Scrpit/
│     ├── EDA.py
│     ├── modeling.py
│     └── ...
├── Readme.md 
├── requirements.txt

```
## Technologies Used

- Python
- PostgreSQL
- SQLAlchemy
- python notebook
- TensorFlow
- PyTorch


## Setup and Installation

1. **Clone the repository:**
    ```sh
   git clone https://github.com/abigiyaayele/Rossamn_retail_sales_prediction.git
    cd Rossamn_retail_sales_prediction
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Approaches

###  1: Exploration of Customer Purchasing Behavior
- Data Cleaning
- Exploratory Data Analysis (EDA)
###  2: Prediction of Store Sales
- Model Building with Sklearn Pipelines
###  3: Building Model with Deep Learning
- LSTM Regression Model
## Deliverables

1. **Exploratory Analysis Notebook**:
   - A comprehensive notebook answering the exploratory questions with visualizations and insights.

2. **Machine Learning Model**:
   - Serialized sklearn model with feature importance analysis and confidence intervals.

4. **Deep Learning Model**:
  - LSTM regression model trained on time series data.

5. **Web Interface**:
  - An interface for serving the predictions to the finance team.


## Author: Abigiya Ayele.
