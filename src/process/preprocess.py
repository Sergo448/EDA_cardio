import os
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tabulate import tabulate
""" более красивый внешний вид графиков по умолчанию """
sns.set()

def get_data(path: str, debug: bool) -> pd.DataFrame:
    """
    Функция, которая читает датасет и выводит первые 10 строк.
    
    :param:
        :path: Path to dataset;
        :type path: str, not None;
    
    :return:
        :data: Датасет;
        :rtype data: pd.DataFrame;
    """

    data = pd.read_csv(path, sep=';')
    if not debug:
        """ head """
        print('$ data head')
        print(tabulate(data.iloc[:10], headers = 'keys', tablefmt = 'psql', showindex=False))
        """ tail """
        print('$ data tail')
        print(tabulate(data.iloc[-10:], headers = 'keys', tablefmt = 'psql', showindex=False))

    return data

def get_info_and_save_to_txt(data: pd.DataFrame, result_path: str, debug: bool) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    result_name: str = 'df.info.txt'
    if not debug:
        print(tabulate(data.info(), headers = 'keys', tablefmt = 'psql', showindex=False))
    
    """ saving results """
    path: str = os.path.join(result_path, result_name)
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Result path: {path}')    
    with open(path, 'w+') as info_file:
        data.info(buf=info_file)
        info_file.close()
        
    return None
    
    
def describe_and_save_to_json(data: pd.DataFrame, result_path: str, debug: bool) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
    """
    result_name: str = 'df.describe.json'
    if not debug:
        print(tabulate(data.describe().T, headers = 'keys', tablefmt = 'psql', showindex=False))
    
    """ saving results """
    path: str = os.path.join(result_path, result_name)
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Result path: {path}')    
    with open(path, 'w+') as info_file:
        data.describe().T.to_json(path_or_buf=path, orient="table")
        info_file.close()
        
    return None

def count_null_values(data: pd.DataFrame, result_path: str) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        result_path (str): _description_
    """
    local_res: dict = dict()
    result_name: str = 'null_not_null.json'
    for column in data.columns:
        null_values: int = int(data[f'{column}'].isnull().sum())
        not_null_values: int = int(data[f'{column}'].notnull().sum())
        info_str: str =\
        f"""
        
        column: {column};
        null_values: {null_values}
        not_null_values: {not_null_values}
        """
        print(info_str)
        local_res[column] = dict({
            'null_values': null_values,
            'not_null_values': not_null_values
            })
        
    path: str = os.path.join(result_path, result_name)
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Result path: {path}')  
    with open(path, 'w+') as info_file:
        json.dump(local_res, info_file)
        info_file.close()
    
    return None

def print_values_in_df(data: pd.DataFrame, result_path: str) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        result_path (str): _description_
    """
    
    local_res: dict = dict()
    result_name: str = 'values_in_fields.json'
    
    for column in data.columns:
        
        print(f'\n$ COLUMN: {column}')
        print(data[f'{column}'].value_counts())
        
        values: list = data[f'{column}'].value_counts().keys().tolist()
        counts: list = data[f'{column}'].value_counts().tolist()
        value_dict: dict = dict(zip(values, counts))
        local_res[f'{column}'] = value_dict
        
    path: str = os.path.join(result_path, result_name)
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Result path: {path}')  
    with open(path, 'w+') as info_file:
        json.dump(local_res, info_file)
        info_file.close()
        
    return None