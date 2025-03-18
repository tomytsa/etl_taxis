import argparse
from etl.extract import extract_data
from etl.load import load_data

file_path = 'data/yellow_tripdata_2021-01.csv'

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name

    df = extract_data(file_path)
    load_data(file_path, user, password, host, port, db, table_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cargar CSV a Postgres')
    parser.add_argument('--user', required=True, help='usuario para Postgres')
    parser.add_argument('--password', required=True, help='password para Postgres')
    parser.add_argument('--host', required=True, help='host para Postgres')
    parser.add_argument('--port', required=True, help='port para Postgres')
    parser.add_argument('--db', required=True, help='db para Postgres')
    parser.add_argument('--table_name', required=True, help='table_name para Postgres')
    args = parser.parse_args()
    main(args)