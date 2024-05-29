# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load data
def load_data(train_path, test_path, store_path):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    store = pd.read_csv(store_path)
    return train, test, store

# Data cleaning: Handling missing values
def handle_missing_values(df):
    imputer = SimpleImputer(strategy='median')
    df['CompetitionDistance'] = imputer.fit_transform(df[['CompetitionDistance']])
    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(0)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(0)
    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
    df['PromoInterval'] = df['PromoInterval'].fillna(0)
    return df

# Data cleaning: Detect and handle outliers
def handle_outliers(df):
    # Example: Removing outliers in sales using IQR method
    Q1 = df['Sales'].quantile(0.25)
    Q3 = df['Sales'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['Sales'] >= (Q1 - 1.5 * IQR)) & (df['Sales'] <= (Q3 + 1.5 * IQR))]
    return df

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
    train = handle_missing_values(train)
    train = handle_outliers(train)

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
