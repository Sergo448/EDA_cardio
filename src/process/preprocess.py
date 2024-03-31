import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import src.config as config
""" более красивый внешний вид графиков по умолчанию """
sns.set()

def get_data(path: str) -> pd.DataFrame:
    """

    :param path: Path to dataset;
    :type path: str, not None;
    
    :return: data
    :rtype data: pd.DataFrame;
    """

    data = pd.read_csv(config.DATA_PATH, sep=';')
    
    return data