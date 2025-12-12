# src/stats_utils.py
"""
Statistical analysis utilities for Iris dataset.
"""

import numpy as np
import pandas as pd
from scipy import stats


def compute_species_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute summary statistics for each species across all measurements.
    
    Args:
        df: Iris dataset DataFrame
    
    Returns:
        pd.DataFrame: Statistics (mean, std, min, max) by species
    """
    numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    stats_dict = {}
    
    for species in df['species'].unique():
        species_data = df[df['species'] == species][numeric_cols]
        stats_dict[species] = {
            'mean': species_data.mean(),
            'std': species_data.std(),
            'min': species_data.min(),
            'max': species_data.max()
        }
    
    return pd.DataFrame(stats_dict).T.round(3)


def perform_anova_test(df: pd.DataFrame, feature: str) -> dict:
    """
    Perform one-way ANOVA test for a feature across species.
    
    Args:
        df: Iris dataset DataFrame
        feature: Feature column to test
    
    Returns:
        dict: ANOVA results (F-statistic, p-value)
    """
    groups = [group[feature].values for name, group in df.groupby('species')]
    f_stat, p_value = stats.f_oneway(*groups)
    return {'F': f_stat, 'p': p_value}
