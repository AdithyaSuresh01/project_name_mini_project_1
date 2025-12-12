# src/data_loader.py
"""
Module for loading the Iris dataset.
"""

from pathlib import Path
import pandas as pd

from .config import DATA_PATH


def load_iris_data() -> pd.DataFrame:
    """
    Load the Iris dataset from CSV file.
    
    Returns:
        pd.DataFrame: Iris dataset with measurements and species labels
    """
    df = pd.read_csv(DATA_PATH / 'iris.csv')
    return df


def get_species_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Get count of samples per species.
    
    Args:
        df: Iris dataset DataFrame
    
    Returns:
        pd.Series: Species counts
    """
    return df['species'].value_counts()
