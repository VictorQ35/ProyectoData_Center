

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    print("ENTRO A LA CONEXION")
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="roundhouse.proxy.rlwy.net",
                #host="viaduct.proxy.rlwy.net",
            port=23300,
            user="root",
            passwd="56HE333E3b2Fa6abE4abCe6ff3-G-F3-",
                #passwd="-D2eD6aDb5Bg6dEbhAAeBB6gd3EheaBg",
            database="railway",
                #database="crud_python",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True

        )
        if connection.is_connected():
            print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
