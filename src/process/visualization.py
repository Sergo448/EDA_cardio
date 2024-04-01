import os
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tabulate import tabulate
""" более красивый внешний вид графиков по умолчанию """
sns.set()

def height_hist_bins_20(data: pd.DataFrame, result_path: str) -> None:
    
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
    
    name: str = 'weight_hist_bins_20.png'
    path: str = os.path.join(result_path, name)
    
    if os.path.exists(path):
        os.remove(path)
    
    print(f'$ Building plot for {name}')
    data['weight'].plot.hist(bins=20, legend=name).get_figure().savefig(path)

    print(f'$  Saving {name} to {path}')
    return None
        
def visualize_plots(data: pd.DataFrame, result_path: str, plot: str) -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        result_path (str): _description_
    """
   
        
    if plot == 'height_hist_bins_20':
        
        name: str = f'{plot}.png'
        path: str = os.path.join(result_path, name)
        if os.path.exists(path):
            os.remove(path)
        
        print(f'$ Building plot for {name}')
        image = data['height'].hist(bins=20, legend=name)

        print(f'$  Saving {name} to {path}')
        image.get_figure().savefig(path)
        
    elif plot == 'weight_hist_bins_20':
        
        name: str = f'{plot}.png'
        path: str = os.path.join(result_path, name)
        if os.path.exists(path):
            os.remove(path)
            
        print(f'$ Building plot for {name}')
        image = data['weight'].hist(bins=20, legend=name)

        print(f'$  Saving {name} to {path}')
        image.get_figure().savefig(path)
    else:
        raise ValueError(f'plot param must be in []')
    
    