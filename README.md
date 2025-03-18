# ETL - Taxis de New York

En este proyecto busque desarrollar un proceso ETL, que pase un archivo CSV a una base de datos PostgreSQL. Fue interesante ya que el CSV tenia millones de filas, entonces tuve que dividirlos en chunks con Pandas. 

## Requisitos

- Docker
  
Opte por dockerizar la aplicación, ya que habia empezado a tener problemas con las versiones de Python, y Docker es una excelente herramienta para solucionar este problema. La otra opcion es una VM, pero los contenedores de Docker son mucho mas livianos

## Configuración

1. Lo primero que hay que hacer es clonar el repositorio 

    ```sh
    git clone https://github.com/tomytsa/etl_taxis
    cd etl_taxis
    ```

2. Hay que crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

    ```env
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    PGADMIN_DEFAULT_EMAIL=
    PGADMIN_DEFAULT_PASSWORD=
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

1. Como primer paso, construimos la imagen de Docker, las instrucciones que le damos estan en el Dockerfile

    ```sh
    docker build -t my_etl_taxi .
    ```

2. Levanta los servicios de Docker Compose:

    ```sh
    docker-compose up -d
    ```

3. Por ultimo, corremos el contenedor my_etl_taxi (el script para subir los datos a PostgreSQL), tenemos que completar las variables con los mismos datos que en el archivo .env:

    ```sh
    docker run -it --network=etl_taxi_default my_etl_taxi --user= --password= --host= --port= --db= --table_name=yellow_taxi_data
    ```

## Verificación

1. Accede a pgAdmin en tu navegador web en `http://localhost:8081`.
2. Inicia sesión con las credenciales configuradas en el archivo `.env`.
3. Conéctate a la base de datos PostgreSQL y verifica que los datos estén presentes en la tabla `yellow_taxi_data`.

## Notas

- Lo mas importante es tener instalado Docker Desktop, en Windows y Mac se instala con Docker-Compose, en Linux hay que instalar las dos cosas por separado.
- La carpeta `data` y el archivo `yellow_tripdata_2021-01.csv` no se subirán a GitHub debido a su tamaño. Asegúrate de tenerlos localmente antes de ejecutar los comandos.
- El proceso funciona para cualquier archivo CSV, no es necesario tener el mismo que yo, lo que hay que hacer si usas un archivo diferente al mio es cambiar la variable file_path en main.py, otra opcion seria agregar esa variable en el comando docker run
- Lo ultimo que hay que tener en cuenta es los contenedores de PostgreSQL, PGADMIN y de Python, tienen que correrse en la misma network, los primeros dos, estan en la misma network por defecto porque los levante con docker-compose, pero el de python hay que agregarlo, por eso en el comando docker run agregue la variable --network=etl_taxi_default (docker-compose por defecto te crea una network con el nombre de la carpeta y _default al final)
