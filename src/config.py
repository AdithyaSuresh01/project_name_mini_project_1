# src/config.py
"""
Project configuration and paths.
"""

from pathlib import Path

# Data directory
DATA_DIR = Path(__file__).parent.parent / 'data'
DATA_PATH = DATA_DIR / 'iris.csv'

# Reports directory
REPORTS_DIR = Path(__file__).parent.parent / 'reports'
FIGURES_PATH = REPORTS_DIR / 'figures'
FIGURES_PATH.mkdir(parents=True, exist_ok=True)

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)
