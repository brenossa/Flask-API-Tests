from flask import render_template
from app import app
from app import database

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/clientes")
def listar_clientes():
    clientes = database.Cliente.query.all()
    return render_template("clientes.html", clientes=clientes)
