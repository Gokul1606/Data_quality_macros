import pandas as pd
import numpy as np

# Function to check for missing values - COMPLETENESS
def missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    missing_percentage = missing / len(df) * 100
    missing_info = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percentage})
    return missing_info

# Function to check for duplicates - UNIQUENESS
def duplicates(df):
    total_duplicates = df.duplicated().sum()
    duplicate_rows = df[df.duplicated()]
    return total_duplicates, duplicate_rows

# Function to check for invalid amounts - CONSISTENCY
def invalid_amounts(df, column):
    invalid_amounts = df[df[column] < 0]
    if len(invalid_amounts) == 0:
        return 'No invalid amounts found'
    else:
        return invalid_amounts

# Funtion to check invalid dates - CONSISTENCY
def invalid_dates(df):
    invalid_dates = []
    for index, row in enumerate(df['Date']):
        try:
            pd.to_datetime(row)
        except:
            invalid_dates.append(index)
    return df.loc[invalid_dates]

# Data Quality rules for stock data
# Finding inconsistent HIGH values in stock data
def inconsistent_high_values(df):
    inconsistent_high_values = df[
        (df['High'] < df['Low']) |
        (df['High'] == 0) |
        (df['High'] > 2 * df['Open'])
    ]
    return inconsistent_high_values

# Finding inconsistent HIGH values in stock data
def inconsistent_low_values(df):
    inconsistent_low_values = df[
        (df['Low'] > df['High']) |
        (df['Low'] == 0) |
        (df['Low'] < 0.5 * df['Open'])
    ]
    return inconsistent_low_values

# Finding inconsistent Open values in stock data
def inconsistent_open_values(df):
    inconsistent_open_values = df[
        (df['Open'] == 0) |
        (df['Open'] > df['High']) |
        (df['Open'] < df['Low']) |
        (df['Open'] < 0)
    ]
    return inconsistent_open_values

# Finding inconsistent Close values in stock data
def inconsistent_close_values(df):
    inconsistent_close_values = df[
        (df['Close'] == 0) |
        (df['Close'] > df['High']) |
        (df['Close'] < df['Low']) |
        (df['Close'] < 0)
    ]
    return inconsistent_close_values

# Finding inconsistent Volume values in stock data
def inconsistent_Volume_values(df):
    df['Volume'] = df['Volume'].fillna(0)
    df['Volume'] = df['Volume'].astype('int')
    # Finding outliers through IQR method
    iqr = df['Volume'].quantile(0.75) - df['Volume'].quantile(0.25)
    Floor_value = df['Volume'].quantile(0.25) - 1.5 * iqr
    Ceiling_value = df['Volume'].quantile(0.75) + 1.5 * iqr
    
    inconsistent_Volume_values = df[
        (df['Volume'] > Ceiling_value) |
        (df['Volume'] < Floor_value)
    ]
    return inconsistent_Volume_values

# Finding inconsistent currency values in stock data
def inconsistent_Currency_values(df):
    inconsistent_currency_values = df[
        ~(df['Currency'] == 'CAD')
    ]
    return inconsistent_currency_values
