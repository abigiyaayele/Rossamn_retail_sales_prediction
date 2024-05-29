# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import logging
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load data
def load_data(train_path, test_path, store_path):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    store = pd.read_csv(store_path)
    return train, test, store

class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, target_column):
        self.target_column = target_column
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        Q1 = X[self.target_column].quantile(0.25)
        Q3 = X[self.target_column].quantile(0.75)
        IQR = Q3 - Q1
        return X[(X[self.target_column] >= (Q1 - 1.5 * IQR)) & (X[self.target_column] <= (Q3 + 1.5 * IQR))]

def build_data_pipeline():
    numeric_features = ['CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 
                        'Promo2SinceWeek', 'Promo2SinceYear']
    
    categorical_features = ['PromoInterval']
    
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ])
    
    outlier_remover = OutlierRemover(target_column='Sales')
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    data_pipeline = Pipeline(steps=[
        ('outlier_remover', outlier_remover),
        ('preprocessor', preprocessor)
    ])
    
    return data_pipeline

# Exploratory Data Analysis: Distribution Analysis
def compare_promo_distribution(train, test):
    sns.histplot(train['Promo'], kde=False, label='Train')
    sns.histplot(test['Promo'], kde=False, color='orange', label='Test')
    plt.legend()
    plt.title('Promotion Distribution in Train and Test Sets')
    plt.show()

# Sales behavior before, during, and after holidays
def sales_during_holidays(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    holidays = df[df['StateHoliday'] != '0']
    sns.lineplot(data=df, x='Date', y='Sales', label='All Sales')
    sns.lineplot(data=holidays, x='Date', y='Sales', label='Holiday Sales')
    plt.title('Sales Before, During, and After Holidays')
    plt.show()

# Seasonal Purchase Behavior
def seasonal_sales_behavior(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    sns.boxplot(x='Month', y='Sales', data=df)
    plt.title('Seasonal Sales Behavior')
    plt.show()

# Correlation Analysis
def correlation_analysis(df):
    correlation = df[['Sales', 'Customers']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation between Sales and Number of Customers')
    plt.show()

# Promo Effectiveness
def promo_effectiveness(df):
    promo_sales = df[df['Promo'] == 1]['Sales']
    no_promo_sales = df[df['Promo'] == 0]['Sales']
    sns.histplot(promo_sales, kde=True, label='Promo')
    sns.histplot(no_promo_sales, kde=True, color='orange', label='No Promo')
    plt.legend()
    plt.title('Effectiveness of Promotions')
    plt.show()

# Operational Trends
def operational_trends(df):
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    sns.boxplot(x='DayOfWeek', y='Sales', data=df)
    plt.title('Sales Trends by Day of Week')
    plt.show()

# Assortment and Competition Analysis
def assortment_effect(df):
    sns.boxplot(x='Assortment', y='Sales', data=df)
    plt.title('Effect of Assortment Type on Sales')
    plt.show()

def competition_effect(df):
    sns.scatterplot(x='CompetitionDistance', y='Sales', data=df)
    plt.title('Effect of Competition Distance on Sales')
    plt.show()

# Main function to run the analysis
def main():
    # Load data
    train, test, store = load_data('train.csv', 'test.csv', 'store.csv')

    # Merge data
    train = pd.merge(train, store, on='Store')
    test = pd.merge(test, store, on='Store')

    # Data Cleaning
     #Data Cleaning using pipeline
    data_pipeline = build_data_pipeline()
    train_cleaned = data_pipeline.fit_transform(train)
    # EDA
    compare_promo_distribution(train, test)
    sales_during_holidays(train)
    seasonal_sales_behavior(train)
    correlation_analysis(train)
    promo_effectiveness(train)
    operational_trends(train)
    assortment_effect(train)
    competition_effect(train)

if __name__ == "__main__":
    main()
