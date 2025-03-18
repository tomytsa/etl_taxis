from sqlalchemy import create_engine
from sqlalchemy.types import DateTime
from time import time
import pandas as pd

# Aca defini la funcion para cargar los datos en PostgreSQL, utilice SQLAlchemy para conectarme a la base de datos
def load_data(file_path, user, password, host, port, db, table_name):
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}',
        echo=False,
        connect_args={'client_encoding': 'utf8'}
    )

    # Aca creo la tabla y la mando a la base de datos, ya defino el tipo de dato para las columnas que tienen fechas (estaban en texto)
    df = pd.read_csv(file_path, nrows=1)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace', dtype={
        'tpep_pickup_datetime': DateTime,
        'tpep_dropoff_datetime': DateTime
    })

    # Este paso es muy importante, ya que el archivo CSV tiene mas de un millon de filas, entonces lo mejor es pasarlo por chunks para no sobrecargar la memoria
    df_iter = pd.read_csv(file_path, chunksize=100000)
    for df_chunk in df_iter:
        t_start = time()

        df_chunk['tpep_pickup_datetime'] = pd.to_datetime(df_chunk['tpep_pickup_datetime'])
        df_chunk['tpep_dropoff_datetime'] = pd.to_datetime(df_chunk['tpep_dropoff_datetime'])

        df_chunk.to_sql(name=table_name, con=engine, if_exists='append', index=True)

        t_end = time()
        print(f"Se insertó un chunk..., llevó {t_end - t_start} segundos")

