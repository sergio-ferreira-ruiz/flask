import os, sys
from fab import tanper
from flask import Flask, render_template, abort
app=Flask(__name__)
@app.route('/')
def pintafab():
    try:
        tanteo = open('envivo.csv', 'r')
        parciales, teams = tanper(tanteo)
        tanteo.close()
    except IOError:
        abort(404)
    return render_template('template5.html', teams=teams, parciales=parciales)
if __name__=="__main__":
    app.run()
