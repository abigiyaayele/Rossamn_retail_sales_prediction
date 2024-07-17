# Rossmann Pharmaceuticals Sales Forecasting

## Overview

This project aims to build an end-to-end system for predicting daily sales in Rossmann Pharmaceuticals stores across several cities, six weeks ahead of time. The goal is to provide the finance team with accurate forecasts to help in better planning and decision-making. The solution involves both traditional machine learning and deep learning approaches, ensuring robust and scalable predictions.

### Problem Statement

Rossmann Pharmaceuticals operates multiple stores across different cities. The finance team needs accurate sales forecasts to make informed decisions and allocate resources effectively. Currently, store managers rely on their intuition and experience, but a more data-driven approach is desired.

### Business Need

The finance team at Rossmann Pharmaceuticals currently relies on store managers' experience and judgment to forecast sales. The need for a more systematic and data-driven approach is evident, as accurate sales predictions can significantly impact inventory management, staffing, and promotional strategies.

## approach
###  1: Exploration of Customer Purchasing Behavior
      - Data Cleaning
1. **Handling Missing Values**
2. **Outlier Detection**
      - Exploratory Data Analysis (EDA)

### 2: Prediction of Store Sales
     - Preprocessing

1. **Feature Engineering**:
2. **Scaling**:
   - Model Building with Sklearn Pipelines


###  3: Building Model with Deep Learning
     - LSTM Regression Model

1. **Data Preparation**:
   - Isolate the dataset into time series data and check for stationarity.
   - Transform the data into a supervised learning format using sliding windows.

2. **Scaling**:
   - Scale the data to the range (-1, 1) for better performance with LSTM networks.

3. **Model Building**:
   - Use TensorFlow or PyTorch to build a two-layer LSTM model for sales prediction.
   - Train the model on the prepared time series data.

### Deliverables

1. **Exploratory Analysis Notebook**:
   - A comprehensive notebook answering the exploratory questions with visualizations and insights.

2. **Machine Learning Model**:
   - Serialized sklearn model with feature importance analysis and confidence intervals.

3. **Deep Learning Model**:
   - LSTM regression model trained on time series data.

4. **Web Interface**:
   - An interface for serving the predictions to the finance team.
 
### Project Structure
The repository has a number of files including python scripts, jupyter notebooks, pdfs and text files. Here is their structure with a brief explanation.

**data:**
- the folder where the dataset files are stored
**notebooks:**
- different jupyter notebooks
**root folder:**
- .gitignore: a text file listing files and folders to be ignored
- README.md: Markdown text with a brief explanation of the project and the repository structure.

### Installation guide

   -   git clone https://github.com/abigiyaayele/Rossamn_retail_sales_prediction.git
   -   cd Rossamn_retail_sales_prediction
   -   pip install -r requirements.txt

# author:[Abigiya Ayele].
