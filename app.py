"""Flask app for Cupcakes"""

# Flask imports
from flask import Flask, jsonify, request

# Local imports
from models import db, connect_db, Cupcake

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
@app.route("/api/cupcakes")
def get_all_cupcakes():
    '''Returns JSON of all cupcakes'''
    cupcakes = Cupcake.query.all()
    serialized = [c.to_dict() for c in cupcakes]
    
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<cupcake_id>")
def get_cupcake(cupcake_id):
    '''returns JSON of a single cupcake'''
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.to_dict()
    
    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    '''adds a cupcake to the database. returns the JSON of that cupcake'''
    
    # Pull the parameters from the JSON
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json.get("image", None)
    
    # Make the cupcake and add to the DB
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    
    serialized = new_cupcake.to_dict
    # Return with status code 201
    return ( jsonify(cupcake = serialized), 201 )