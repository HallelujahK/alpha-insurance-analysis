import pandas as pd

def descriptive_statistics(df):
    """
    This function calculates and returns descriptive statistics for numerical features in the dataframe.
    It includes measures of central tendency (mean, median) and variability (variance, standard deviation).
    """

    # Select numerical columns only
    numerical_columns = df.select_dtypes(include=['number']).columns

    # Summary statistics for numerical features
    summary_stats = df[numerical_columns].describe().T
    
    # Adding variability metrics: variance and range (max - min)
    summary_stats['variance'] = df[numerical_columns].var()
    summary_stats['range'] = df[numerical_columns].max() - df[numerical_columns].min()
    
    return summary_stats

def data_structure(df):
    """
    This function returns the data types of each column and checks if categorical, date fields are correctly formatted.
    """

    # Check data types of columns
    dtype_info = df.dtypes

    # Checking for potential date fields
    date_columns = df.select_dtypes(include=['datetime64']).columns

    # Checking for categorical fields
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns

    return {
        "Data Types": dtype_info,
        "Date Columns": date_columns,
        "Categorical Columns": categorical_columns
    }

def check_missing_values(df):
    """
    Check for missing values in the DataFrame.
    
    :param df: pd.DataFrame, input data
    :return: pd.Series, count of missing values per column
    """
    return df.isnull().sum()
