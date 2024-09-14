# src/load_data.py
import pandas as pd

def load_data(filepath):
    """
    Load data from a .txt file that is pipe-delimited.
    
    :param filepath: str, path to the .txt file
    :return: pd.DataFrame, loaded data
    """
    try:
        data = pd.read_csv(filepath, delimiter='|')  # Use '|' as the delimiter
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
