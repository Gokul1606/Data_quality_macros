import pandas as pd
import numpy as np

# Function to check for missing values
def missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    missing_percentage = missing / len(df) * 100
    missing_info = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percentage})
    return missing_info

