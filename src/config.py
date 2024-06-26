import os

DEBUG: bool = True

PROJECT_FOLDER: str = 'P:\\Python Projects\\EDA_cardio'
DATASET_NAME: str = 'cardio_train.csv'
DATA_PATH: str = os.path.join(PROJECT_FOLDER, 'src', 'raw', DATASET_NAME)

RESULT_PATH: str = os.path.join(PROJECT_FOLDER, 'src', 'visualizations')