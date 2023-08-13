from flask import Blueprint, render_template

#! initialize blueprint, always need to pass in __name__, and the name of the blueprint
# views = Blueprint(__name__, "views")
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")