# src/bivariate_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_correlation_matrix(df):
    """
    Plot the correlation matrix for numerical columns.

    :param df: pd.DataFrame, input data
    """
    # Convert any date columns to datetime format
    if 'TransactionDate' in df.columns:
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

    # Select only numerical columns for correlation matrix
    numerical_cols = df.select_dtypes(include=['number']).columns
    plt.figure(figsize=(12, 8))
    corr = df[numerical_cols].corr()

    # Plot heatmap
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def scatter_plot(df, x_col, y_col, hue_col=None):
    """
    Scatter plot between two numerical columns.
    
    :param df: pd.DataFrame, input data
    :param x_col: str, x-axis column
    :param y_col: str, y-axis column
    :param hue_col: str, column for hue (optional)
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
    plt.title(f"{y_col} vs {x_col}")
    plt.show()
