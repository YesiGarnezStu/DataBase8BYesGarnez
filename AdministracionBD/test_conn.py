import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="clase123",
        database="escuela_db"
    )

    print("Conexión exitosa a MySQL")

    conn.close()

except Exception as e:
    print("Error:", e)