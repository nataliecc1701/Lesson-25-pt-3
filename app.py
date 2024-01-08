"""Flask app for Cupcakes"""

# Flask imports
from flask import Flask, render_template, redirect, flash, request

# Local imports
from models import connect_db, Cupcake

app = Flask(__name__)

# pull our config parameters from a text file
with open("config.txt") as config:
    for line in config:
        params=line.split()
        
        # parse string to bools
        if params[1] == "True":
            params[1] = True
        elif params[1] == "False":
            params[1] = False
        
        # apply to app.config
        app.config[params[0]] = params[1]
        
connect_db(app)

# Routes