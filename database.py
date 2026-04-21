import sqlite3

def get_conn():
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
    conn.commit()
    conn.close()   