from flask import Flask, request, render_template, redirect, url_for
from database import init_db, get_conn

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    conn = get_conn()
    # SELECT * trae todos los registros de la tabla
    cursor = conn.execute("SELECT * FROM productos")
    productos = cursor.fetchall()  # guarda todos en una lista
    conn.close()
    return render_template("index.html", productos=productos) 

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST": 
        nombre    = request.form.get("nombre")
        categoria = request.form.get("categoria")
        precio    = request.form.get("precio")
        stock     = request.form.get("stock")
        conn = get_conn()
        conn.execute(
            "INSERT INTO productos(nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
            (nombre, categoria, precio, stock)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("agregar.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = get_conn()

    if request.method == "POST": 
        nombre    = request.form.get("nombre")
        categoria = request.form.get("categoria")
        precio    = request.form.get("precio")
        stock     = request.form.get("stock")
        conn.execute(
            "UPDATE productos SET nombre=?, categoria=?, precio=?, stock=? WHERE id=?",
            (nombre, categoria, precio, stock, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    cursor = conn.execute("SELECT * FROM productos WHERE id=?", (id,))
    producto = cursor.fetchone()  # fetchone trae solo un registro
    conn.close()
    return render_template("editar.html", producto=producto)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = get_conn()
    conn.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)