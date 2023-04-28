""" Solución al reto de la Unidad de Fomentos""

1) Primeramente debemos instalar desde la consola lo siguiente:

    pip install fastapi 
    pip install uvicorn
    pip install psycopg2
    pip install SQLAlchemy

Para crear la base de datos y llenar sus datos lo podemos hacer de dos maneras:

a) Utilice una base de datos postgres, para crear la tabla y llenar los datos por medio de un script sql llamado create_db.sql que se encuentra en la carpeta inititalization_script y luego ejecute el archivo script.py:

        cd app/initialization_script
        python script.py

b) Para ejecutar correctamente el archivo script.py, debemos primero ir a postgres y crear una base de datos con la siguiente configuracion

    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres",
    port="5432",

    si el "port" que te genera postgres por defecto en tu pc no es "5432" debes cambiarlo manualamente sino te funciona deja el que te 
    coloca postgres por defecto y ve a la carpeta: /app/initialization_script/script.py, de esta manera accederás al archivo python de
    configuración de conexión con la base de datos postgres, una vez alli debes cambiar el valor de "port" por el que te genera tu pc 
    por defecto.

    Una vez ya creada la base de datos con la configuracion correcta puedes proceder a ejecutar el archivo script.py que se encuentra en la ruta antes mencionada.

    ------------------------------------------------------------------------------------------------------------------------------------
    
    Al realizar la conexión con éxito con alguno de los dos método el a o el b, verás en tu base de datos postgres como automáticamente se crean las tablas y los valores para trabajar con el reto UF.

    una vez listo procedemos a encender el servidor con el siguiente comando desde la consola
    
        uvicorn main:app --reload

    Finalmente, pasas al método http://localhost:8000/get-uf-by-date para ingresar una fecha como parámetro y por medio de esa fecha te arrojara como resultado el valor de la unidad de fomentos correspondiente a la fecha ingresada 

    Ejemplo:
    
    Fecha ingresada correctamente:
    http://localhost:8000/get-uf-by-date?date=2023-11-01T00:00:00
    http://localhost:8000/get-uf-by-date?date=2023-10-01T00:00:00
    http://localhost:8000/get-uf-by-date?date=2023-05-01T00:00:00

