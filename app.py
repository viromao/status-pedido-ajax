from webbrowser import get
from flask import Flask, jsonify, render_template
import oracle_connect
import getPedidos
import time


app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("homepage.html")


@app.route("/teste")
def teste():
    qtdemitido = oracle_connect.consultaQtdeEmitido().fetchone()[0]
    qtdsep = oracle_connect.consultaQtdEmSeparacao().fetchone()[0]
    qtdemconf = oracle_connect.consultaQtdeEmConferencia().fetchone()[0]
    qtdconf = oracle_connect.consultaQtdeConferido().fetchone()[0]
    lista = getPedidos.novosPedidos()

    return jsonify(qtdaberto=qtdemitido, qtdsep=qtdsep, qtdemconf=qtdemconf,qtdconf=qtdconf, lista=lista)




   

if __name__ == "__main__":
    app.run(  debug = False, host="0.0.0.0", port="80")

