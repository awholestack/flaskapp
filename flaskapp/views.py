from flask import Blueprint, jsonify

data = Blueprint("data", __name__, url_prefix="/data")

data = Blueprint()


@data.route("/")
def data_index():
    return jsonify({"Data": "Hello World"})
