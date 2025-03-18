import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo CSV no se encontro en {file_path}...")