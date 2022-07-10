from flask import Blueprint

ROUTE = Blueprint('ROUTE',__name__)

@ROUTE.route("/home", methods=["GET"])
def home_page():
    return "hello hi this is an AI web page"