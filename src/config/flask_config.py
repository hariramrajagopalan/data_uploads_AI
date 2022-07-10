from flask import Flask
from data_uploads_rest.rest_data_uplaods import ROUTE

APP = Flask(__name__)

def register_blueprints():
    APP.register_blueprint(ROUTE)
    
register_blueprints()