import psycopg2


connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres",
    port="5432",   
)

connection.autocommit = True

def createTable():
    cursor = connection.cursor()
    query = "CREATE TABLE unidad(id serial, date date, unidad_de_fomento float8)"
    try:
        cursor.execute(query)
    except:
        print("el valor ingresado en la tabla ya existe")
    cursor.close()


def insertData():
    cursor = connection.cursor()
    query = """ INSERT INTO unidad(date,unidad_de_fomento) values ('1/01/2023','35122.26'), ('1/02/2023','35290.91'),
    ('1/03/2023','35574.33'),('1/04/2023','35851.62'),('1/05/2023','35133.53'),('1/06/2023','35219.73'),('1/07/2023','31519.69'),
    ('1/08/2023','35319.22'),('1/09/2023','12319.79'),('1/10/2023','232319.79'),('1/11/2023','21319.79'),('1/12/2023','32519.39')
    """
    cursor.execute(query)
    cursor.close()

createTable()
insertData()



