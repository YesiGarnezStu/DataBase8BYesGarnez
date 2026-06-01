import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="clase123",
    database="escuela_db"
)

cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    carrera VARCHAR(100)
)
""")

print("✅ Tabla creada")

# Insertar datos
datos = [
    ("Ana López", 20, "Ingeniería"),
    ("Carlos Ruiz", 22, "Medicina"),
    ("María Torres", 19, "Diseño Gráfico")
]

cursor.executemany(
    "INSERT INTO estudiantes (nombre, edad, carrera) VALUES (%s, %s, %s)",
    datos
)

conn.commit()

print("✅ Datos insertados")

# Mostrar datos
cursor.execute("SELECT * FROM estudiantes")

print("\n📚 LISTA DE ESTUDIANTES:\n")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conn.close()