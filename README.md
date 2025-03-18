# ETL Taxis

En este proyecto busque desarrollar un proceso ETL, que pase un archivo CSV a una base de datos PostgreSQL. Fue interesante ya que el CSV tenia millones de filas, entonces tuve que dividirlos en chunks con Pandas. 

## Requisitos

- Docker
  
Opte por dockerizar la aplicación, ya que habia empezado a tener problemas con las versiones de Python, y Docker es una excelente herramienta para solucionar este problema. La otra opcion es una VM, pero los contenedores de Docker son mucho mas livianos

## Configuración

1. Clona el repositorio:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

    ```env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=mysecretpassword
    POSTGRES_DB=postgres
    PGADMIN_DEFAULT_EMAIL=admin@admin.com
    PGADMIN_DEFAULT_PASSWORD=root
    ```

3. Asegúrate de que la carpeta `data` y el archivo `yellow_tripdata_2021-01.csv` estén presentes en el directorio correcto.

4. Agrega las siguientes líneas a tu archivo `.gitignore` para evitar subir archivos sensibles y grandes:

    ```gitignore
    .env
    postgres-data/
    pgadmin-data/
    data/
    ```

## Construcción y Ejecución

1. Construye la imagen Docker:

    ```sh
    docker build -t my_etl_taxi .
    ```

2. Levanta los servicios de Docker Compose:

    ```sh
    docker-compose up -d
    ```

3. Ejecuta el contenedor Docker para cargar los datos en la base de datos:

    ```sh
    docker run -it --network=docker_sql_default my_etl_taxi --file_path=data/yellow_tripdata_2021-01.csv --user=postgres --password=mysecretpassword --host=pgdatabase --port=5432 --db=postgres --table_name=yellow_taxi_data
    ```

## Verificación

1. Accede a pgAdmin en tu navegador web en `http://localhost:8081`.
2. Inicia sesión con las credenciales configuradas en el archivo `.env`.
3. Conéctate a la base de datos PostgreSQL y verifica que los datos estén presentes en la tabla `yellow_taxi_data`.

## Notas

- Asegúrate de que Docker y Docker Compose estén instalados en tu máquina.
- La carpeta `data` y el archivo `yellow_tripdata_2021-01.csv` no se subirán a GitHub debido a su tamaño. Asegúrate de tenerlos localmente antes de ejecutar los comandos.
