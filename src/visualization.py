import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_content_distribution(df, save_path=None):
    """
    Визуализация распределения контента по типам
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    type_counts = df['type'].value_counts()
    
    # Круговая диаграмма
    ax1.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Соотношение Фильмов и Сериалов')
    
    # Столбчатая диаграмма
    sns.countplot(data=df, x='type', ax=ax2)
    ax2.set_title('Количество по типам')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
