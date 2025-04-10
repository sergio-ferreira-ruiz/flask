import os, sys
from fab import tanper
from flask import Flask
app=Flask(__name__)
@app.route('/')
def pintafab():
    estadif=open('envivo.csv','r')
    cuartos,teams= tanper(estadif)
    salida=''
    for cuarto, parcial in cuartos.items():
        salida+='{}º Cuarto.&emsp;'.format(cuarto)
        for equipo, puntos in parcial.items():            
            salida+='{}:&ensp;{}&emsp;'.format(teams[equipo],puntos)
        salida+='<hr>'
    estadif.close()
    return salida
if __name__=="__main__":
    app.run()
