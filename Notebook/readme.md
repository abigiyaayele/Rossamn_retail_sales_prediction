# Rossmann Pharmaceuticals Sales Forecasting


## Data and Features

The dataset consists of various features, including:

- Id - an Id that represents a (Store, Date) duple within the test set
- Store - a unique Id for each store
- Sales - the turnover for any given day (this is what you are predicting)
- Customers - the number of customers on a given day
- Open - an indicator for whether the store was open: 0 = closed, 1 = open
- StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
- StoreType - differentiates between 4 different store models: a, b, c, d
- Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
- CompetitionDistance - distance in meters to the nearest competitor store
- CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
- Promo - indicates whether a store is running a promo on that day
- Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
- Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
- PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store
  
## approach
###  1: Exploration of Customer Purchasing Behavior
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

### 2: Prediction of Store Sales

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

### 3: Building Model with Deep Learning

#### LSTM Regression Model

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


# author:[Abigiya Ayele].

