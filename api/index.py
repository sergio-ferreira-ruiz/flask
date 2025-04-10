import os
from flask import Flask, render_template, abort
from .fab import tanper  # Importa desde submódulo si fab.py está en la carpeta api

app = Flask(__name__)

@app.route('/')
def pintafab():
    try:
        # Construye la ruta del archivo correctamente
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'envivo.csv')
        tanteo = open(file_path, 'r')
        parciales, teams = tanper(tanteo)  # Asegúrate de que tanper devuelva en este orden
        tanteo.close()
    except IOError:
        abort(404)
    return render_template('template5.html', teams=teams, parciales=parciales)

# Es muy importante para Vercel añadir:
@app.route('/<path:path>')
def catch_all(path):
    return abort(404)
