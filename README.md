# Rossamn_retail_sales_prediction
10 academy week 5 project
## Project Summary

Sales Forecasting System for Rossmann Pharmaceuticals

### Overview

This project aims to build an end-to-end system for predicting daily sales in Rossmann Pharmaceuticals stores across several cities, six weeks ahead of time. The goal is to provide the finance team with accurate forecasts to help in better planning and decision-making. The solution involves both traditional machine learning and deep learning approaches, ensuring robust and scalable predictions.

### Problem Statement

Rossmann Pharmaceuticals operates multiple stores across different cities. The finance team needs accurate sales forecasts to make informed decisions and allocate resources effectively. Currently, store managers rely on their intuition and experience, but a more data-driven approach is desired.

### Business Need

The finance team at Rossmann Pharmaceuticals currently relies on store managers' experience and judgment to forecast sales. The need for a more systematic and data-driven approach is evident, as accurate sales predictions can significantly impact inventory management, staffing, and promotional strategies.

### Data and Features

The dataset consists of various features, including:
- Store details (Store ID, StoreType, Assortment)
- Sales and customer data (Sales, Customers)
- Indicators for store operations (Open, Promo, Promo2)
- Holiday and competition information (StateHoliday, SchoolHoliday, CompetitionDistance, CompetitionOpenSince, PromoInterval)
- Seasonality: Monthly and yearly patterns in sales.

### Task 1: Exploration of Customer Purchasing Behavior

#### Data Cleaning

1. **Handling Missing Values**: Identify and fill missing values, especially in `CompetitionDistance`, `CompetitionOpenSince`, `Promo2Since`, and `PromoInterval`.
2. **Outlier Detection**: Use statistical methods and visualizations to detect and handle outliers.

#### Exploratory Data Analysis (EDA)

1. **Distribution Analysis**:
   - Compare the distribution of promotions between training and test sets.
   - Visualize sales behavior before, during, and after holidays to identify patterns.

2. **Seasonal Purchase Behavior**:
   - Analyze sales during Christmas, Easter, and other significant holidays.

3. **Correlation Analysis**:
   - Examine the correlation between sales and the number of customers.
   - Analyze how promotions affect sales and customer numbers.

4. **Promo Effectiveness**:
   - Determine the effectiveness of different types of promotions.
   - Identify stores where promotions are most beneficial.

5. **Operational Trends**:
   - Explore customer behavior during store opening and closing times.
   - Analyze the impact of store operating days on weekend sales.

6. **Assortment and Competition**:
   - Investigate how different assortment types affect sales.
   - Study the impact of the distance to the nearest competitor on sales.

#### Visualizations

Use plots such as histograms, box plots, scatter plots, and time series plots to visualize the findings from the above analyses.

### Task 2: Prediction of Store Sales

#### Preprocessing

1. **Feature Engineering**:
   - Extract new features from date columns (e.g., weekdays, weekends, days to holidays).
   - Create additional features to capture monthly trends (e.g., beginning, mid, end of the month).

2. **Scaling**:
   - Apply standard scaling to normalize the features.

#### Model Building with Sklearn Pipelines

1. **Algorithm Selection**:
   - Start with tree-based algorithms like Random Forest Regressor for initial modeling.
   - Use sklearn pipelines for modular and reproducible modeling.

2. **Loss Function**:
   - Choose and justify an appropriate loss function for the regression problem (e.g., Mean Absolute Error for interpretability).

3. **Post Prediction Analysis**:
   - Analyze feature importance to understand the model's decision-making process.
   - Estimate the confidence interval of the predictions for better reliability.

4. **Model Serialization**:
   - Save the trained models with timestamps to track and manage different versions.

### Task 3: Building Model with Deep Learning

#### LSTM Regression Model

1. **Data Preparation**:
   - Isolate the dataset into time series data and check for stationarity.
   - Transform the data into a supervised learning format using sliding windows.

2. **Scaling**:
   - Scale the data to the range (-1, 1) for better performance with LSTM networks.

3. **Model Building**:
   - Use TensorFlow or PyTorch to build a two-layer LSTM model for sales prediction.
   - Train the model on the prepared time series data.

### Conclusion

By following the outlined steps, we aim to deliver a robust and scalable sales prediction system for Rossmann Pharmaceuticals. This system will enable the finance team to make informed decisions based on accurate forecasts, ultimately improving the company's operational efficiency and profitability.

### Next Steps

1. **Deploy the Model**:
   - Serve the model predictions via a web interface accessible to analysts in the finance team.

2. **Monitor and Update**:
   - Continuously monitor the model's performance and update it regularly with new data.

3. **Extend Analysis**:
   - Further explore additional features and refine the models for even better accuracy.

### Deliverables

1. **Exploratory Analysis Notebook**:
   - A comprehensive notebook answering the exploratory questions with visualizations and insights.

2. **Machine Learning Model**:
   - Serialized sklearn model with feature importance analysis and confidence intervals.

3. **Deep Learning Model**:
   - LSTM regression model trained on time series data.

4. **Web Interface**:
   - An interface for serving the predictions to the finance team.


# author:[Abigiya Ayele].