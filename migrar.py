import mysql.connector

# 🔹 Conexión a tu base local (XAMPP)
conexion_local = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cine"
)

# 🔹 Conexión a Railway (con tus credenciales reales)
conexion_railway = mysql.connector.connect(
    host="yamabiko.proxy.rlwy.net",
    port=48353,  # 👈 pon aquí el puerto (ej: 7423)
    user="root",
    password="TjylfiNFADomCuTTsohwhsBrIZkKNpyX",
    database="cine"
)

cursor_local = conexion_local.cursor()
cursor_railway = conexion_railway.cursor()

# ----------------------------------------
# 🔹 Primero migramos la tabla genero
# ----------------------------------------
cursor_local.execute("SELECT * FROM genero")
generos = cursor_local.fetchall()

for genero in generos:
    cursor_railway.execute(
        "INSERT INTO genero (id_genero, nom_genero) VALUES (%s, %s)",
        genero
    )

# ----------------------------------------
# 🔹 Luego migramos la tabla peliculas
# ----------------------------------------
cursor_local.execute("SELECT * FROM peliculas")
peliculas = cursor_local.fetchall()

for peli in peliculas:
    cursor_railway.execute(
        """
        INSERT INTO peliculas 
        (id_pelicula, nom_pelicula, dura_pelicula, doblado, comentario_pelicula, genero_id_genero) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        peli
    )

# Guardar cambios en Railway
conexion_railway.commit()

print("✅ Datos migrados correctamente a Railway 🚀")

conexion_local.close()
conexion_railway.close()
