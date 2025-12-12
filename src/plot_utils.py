# src/plot_utils.py
"""
Visualization utilities for Iris dataset analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pandas as pd

from .config import FIGURES_PATH

plt.style.use('seaborn-v0_8')
sns.set_palette('husl')


def create_pairplot(df: pd.DataFrame, save_path: Path = None) -> plt.Figure:
    """
    Create pairwise scatterplot matrix colored by species.
    
    Args:
        df: Iris dataset DataFrame
        save_path: Path to save figure
    
    Returns:
        plt.Figure: Pairplot figure
    """
    fig = sns.pairplot(df, hue='species', diag_kind='hist')
    fig.fig.suptitle('Iris Dataset - Pairwise Relationships', y=1.02)
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def create_boxplots_by_species(df: pd.DataFrame, save_path: Path = None) -> plt.Figure:
    """
    Create boxplots for all features by species.
    
    Args:
        df: Iris dataset DataFrame
        save_path: Path to save figure
    
    Returns:
        plt.Figure: Boxplot figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    
    for i, feature in enumerate(features):
        ax = axes[i//2, i%2]
        sns.boxplot(data=df, x='species', y=feature, ax=ax)
        ax.set_title(f'{feature.title()} by Species')
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
