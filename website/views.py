from flask import Blueprint

#! initialize blueprint, always need to pass in __name__, and the name of the blueprint
# views = Blueprint(__name__, "views")
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return "<h1>Test</h1>"