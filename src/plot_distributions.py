import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_numerical_distributions(df):
    """
    Plots histograms for each numerical column in the dataset.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    None
    """
    # Automatically select numerical columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    for col in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True, bins=30, color='blue')
        plt.title(f'Distribution of {col}', fontsize=16)
        plt.xlabel(col, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.grid(True)
        plt.show()

def plot_categorical_distributions(df):
    """
    Plots bar charts for each categorical column in the dataset.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    None
    """
    # Automatically select categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    for col in categorical_columns:
        plt.figure(figsize=(8, 6))
        sns.countplot(y=df[col], palette='Set2')
        plt.title(f'Distribution of {col}', fontsize=16)
        plt.xlabel('Count', fontsize=14)
        plt.ylabel(col, fontsize=14)
        plt.grid(True)
        plt.show()
