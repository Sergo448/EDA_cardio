import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tabulate import tabulate
""" более красивый внешний вид графиков по умолчанию """
sns.set()

def height_hist_bins_20(data: pd.DataFrame, result_path: str) -> None:
    """Строим столбчатую диаграмму и сохраняем. Для поля height

    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
        
        :result_path: Path to results;
        :type result_path: str, not None;
    
    :return:
        None
    """
    name: str = 'height_hist_bins_20.png'
    path: str = os.path.join(result_path, name)
    
    if os.path.exists(path):
        os.remove(path)
        
    fig, axs = plt.subplots(figsize=(12, 4))
    print(f'$ Building plot for {name}')
    data['height'].plot.hist(bins=20, legend=name, ax=axs).get_figure().savefig(path)
    fig.savefig(f"xx{path}")
    print(f'$  Saving {name} to {path}')
    return None

def weight_hist_bins_20(data: pd.DataFrame, result_path: str) -> None:
    """Строим столбчатую диаграмму и сохраняем. Для поля weight

    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
        
        :result_path: Path to results;
        :type result_path: str, not None;
    
    :return:
        None
    """
    name: str = 'weight_hist_bins_20.png'
    path: str = os.path.join(result_path, name)
    
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Building plot for {name}')
    data['weight'].plot.hist(bins=20, legend=name).get_figure().savefig(path)

    print(f'$  Saving {name} to {path}')
    return None
        
def print_pivot(data: pd.DataFrame) -> None:
    """Строим сводную таблицу и выводим на экран.
    
    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
    
    :return:
        None
    """
    # values - признаки, по которым вычисляются значения функции aggfunc
    # index - признаки, по которым выполняется группировка
    
    pivot = data.pivot_table(values=['age', 'cardio'], index=['smoke', 'alco'], aggfunc='mean')
    print(tabulate(pivot, headers = 'keys', tablefmt = 'psql', showindex=False))
    return None

def print_aclo_smoke(data: pd.DataFrame) -> None:
    """Строим сводную таблицу и выводим на экран.
    
    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
    
    :return:
        None
    """
    crosstab = pd.crosstab(data['smoke'], data['alco'])
    print(tabulate(crosstab, headers = 'keys', tablefmt = 'psql', showindex=False))
    return None

def mean_smoke_age(data: pd.DataFrame) -> None:
    """Строим сводную таблицу и выводим на экран.
    
    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
    
    :return:
        None
    """
    print('$ Вычислим средний возраст людей, склонных к курению')
    res = data[data['smoke'] == 1]['age'].mean()
    print(f'$ result: {res}')
    return None


def mean_smoke_age_and_cardio(data: pd.DataFrame) -> None:
    """Строим сводную таблицу и выводим на экран.
    
    :param:
        :data: Датасет;
        :type data: pd.DataFrame;
    
    :return:
        None
    """
    print('$ Вычислим средний возраст людей, склонных к курению')
    res = data[(data['smoke'] == 1) & (data['cardio'] == 1)]['age'].mean()
    print(f'$ result: {res}')
    return None
