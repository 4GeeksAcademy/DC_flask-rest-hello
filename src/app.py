"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# --- ENDPOINTS ---

# ----------------------- GET -----------------------

# CHARACTERS

@app.route('/characters', methods=['GET'])
def get_all_characters():

    characters_query = Character.query.all()
    results = list(map(lambda item: item.serialize(), characters_query))

    response_body = {
       "results": results
    }

    return jsonify(response_body), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_one_characters(character_id):

    character_query = Character.query.filter_by(id=character_id).first()
    

    response_body = {
       "results": character_query.serialize()
    }

    return jsonify(response_body), 200

# PLANETS

@app.route('/planets', methods=['GET'])
def get_all_planets():

    planets_query = Planet.query.all()
    results = list(map(lambda item: item.serialize(), planets_query))

    response_body = {
       "results": results
    }

    return jsonify(response_body), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planets(planet_id):

    planet_query = Planet.query.filter_by(id=planet_id).first()
    

    response_body = {
       "results": planet_query.serialize()
    }

    return jsonify(response_body), 200

# USERS

@app.route('/users', methods=['GET'])
def get_all_users():

    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(), users_query))

    response_body = {
       "results": results
    }

    return jsonify(response_body), 200

# @app.route('/users/favoritos', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "results": "Hello, this is favoritos"
#     }

#     return jsonify(response_body), 200

# ----------------------- POST -----------------------
# CHARACTERS

# @app.route('/characters', methods=['POST'])
# def create_character():

#     request_body = request.get_json(force=True)

#     character = Character(name=request_body['name'],
#                           birth_year=request_body['birth_year'],
#                           gender=request_body['gender'], 
#                           height=request_body['height'], 
#                           skin_color=request_body['skin_color'], 
#                           eye_color=request_body['eye_color'])
    

#     db.session.add(character)
#     db.session.commit()


#     response_body = {
#        "results": 'Character Created'
#     }

#     return jsonify(response_body), 200

# PLANETS

# @app.route('/planets', methods=['POST'])
# def create_planet():

#     request_body = request.get_json(force=True)

#     planet = Planet(name=request_body['name'],
#                     climate=request_body['climate'],
#                     population=request_body['population'], 
#                     orbital_period=request_body['orbital_period'], 
#                     rotation_period=request_body['rotation_period'], 
#                     diameter=request_body['diameter'])
    
#     db.session.add(planet)
#     db.session.commit()


#     response_body = {
#        "results": 'Planet Created'
#     }

#     return jsonify(response_body), 200

# USERS

# @app.route('/users', methods=['POST'])
# def create_user():

#     request_body = request.get_json(force=True)

#     user = User(name=request_body['name'],
#                 climate=request_body['climate'],
#                 population=request_body['population'], 
#                 orbital_period=request_body['orbital_period'], 
#                 rotation_period=request_body['rotation_period'], 
#                 diameter=request_body['diameter'])

#     db.session.add(planet)
#     db.session.commit()


#     response_body = {
#        "results": 'Planet Created'
#     }

#     return jsonify(response_body), 200



# --- FIN ENDPOINTS ---

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
