import sqlite3  # libreria de python para manejar bases de datos

def get_conn():
    # crea la conexion al archivo inventario.db
    # si no existe, python lo crea automaticamente
    conn = sqlite3.connect("inventario.db")
    return conn

def init_db():
    conn = get_conn()  # nos conectamos
    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id        INTEGER PRIMARY KEY,  -- numero unico, se pone solo
            nombre    TEXT NOT NULL,        -- nombre del producto
            categoria TEXT NOT NULL,        -- ej: laptop, celular, etc
            precio    REAL NOT NULL,        -- numero con decimales ej: 99.99
            stock     INTEGER NOT NULL      -- cantidad disponible
        )
    """)
    conn.commit()   # guardamos los cambios
    conn.close()    # cerramos la conexion