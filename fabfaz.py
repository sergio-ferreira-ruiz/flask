from flask import Flask
import sys
import os

# Añadimos el directorio padre a sys.path para importar fab.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fab import tanper

app = Flask(__name__)

@app.route('/')
def pintafab():
    try:
        # Obtenenemos la ruta correcta al archivo CSV
        csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'envivo.csv')
        with open(csv_path, 'r', encoding='utf-8') as estadif:
            equipos, periodos = tanper(estadif)
        
        salida = ''
        for cuarto, parcial in periodos.items():
            salida += '{}º Cuarto.&emsp;'.format(cuarto)
            for equipo, puntos in parcial.items():            
                salida += '{}:&ensp;{}&emsp;'.format(equipos[equipo], puntos)
            salida += '<hr>'
        
        return salida
    except Exception as e:
        return f"Error: {str(e)}"

# Esto es importante para Vercel
app.debug = True

# Para pruebas locales
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
