from flask import Flask 
from flask_cors import CORS
from .extensions import mongo
from .main import main

def create_app(config_object='codebase.settings'):
    app = Flask(__name__)

    CORS(app)
    
    app.config.from_object(config_object)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app