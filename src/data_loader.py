import pandas as pd
import numpy as np

def load_netflix_data(file_path):
    """
    Загрузка и базовая подготовка данных Netflix
    """
    df = pd.read_csv(file_path)
    
    # Базовая информация
    print(f"Данные загружены. Размер: {df.shape}")
    print(f"Фильмы: {len(df[df['type'] == 'Movie'])}")
    print(f"Сериалы: {len(df[df['type'] == 'TV Show'])}")
    
    return df

def preprocess_data(df):
    """
    Предварительная обработка данных
    """
    # Преобразование дат
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    
    return df
