import pandas as pd


def delete_wrong_values(data: pd.DataFrame) -> pd.DataFrame:
    """Удаляем неверные значения (слишком большие и слишком маленькие)

    Args:
        data (pd.DataFrame): входязий датафрейм.

    Returns:
        pd.DataFrame: Выходязий датафрейм.
    """
    # Удалим всех пацентов с ростом ниже 125 см, а также выше 200 см
    dummy_df = data.drop(data[(data['height'] < 125) | (data['height'] > 200)].index)
    
    differense = dummy_df.shape[0] / data.shape[0]
    print(f'$ diff: {differense}')
    return dummy_df

def add_height_cm(dummy_df: pd.DataFrame) -> pd.DataFrame:
    """Добавляем столбец рост в см.

    Args:
        data (pd.DataFrame): входязий датафрейм.

    Returns:
        pd.DataFrame: Выходязий датафрейм.
    """
    dummy_df['height_cm'] = dummy_df['height'] / 100
    return dummy_df

def add_dummy_cholesterol(dummy_df: pd.DataFrame) -> pd.DataFrame:
    """Перекодируем столбец с холестерином

    Args:
        data (pd.DataFrame): входязий датафрейм.

    Returns:
        pd.DataFrame: Выходязий датафрейм.
    """
    
    new_values = {1:'low', 2:'normal', 3:'high'} # обычный словарь Python
    dummy_df['dummy_cholesterol'] = dummy_df['cholesterol'].map(new_values)
    return dummy_df

def cardio_astype_bool(dummy_df: pd.DataFrame) -> pd.DataFrame:
    """Перекодируем столбец с целевой переменной.

    Args:
        data (pd.DataFrame): входязий датафрейм.

    Returns:
        pd.DataFrame: Выходязий датафрейм.
    """
    dummy_df['cardio'] = dummy_df['cardio'].astype(bool)
    return dummy_df