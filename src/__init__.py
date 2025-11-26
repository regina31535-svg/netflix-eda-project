"""
Netflix EDA Project - Source Modules
"""

from .data_loader import load_netflix_data, preprocess_data, get_basic_stats
from .visualization import (
    plot_content_distribution,
    plot_top_countries, 
    plot_trends_overtime,
    create_genre_wordcloud,
    plot_rating_distribution
)

__version__ = "1.0.0"
__author__ = "Your Name"
