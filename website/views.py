from flask import Blueprint, render_template, request, flash, redirect, url_for


views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html", mathURL=url_for("views.math"), physicsURL=url_for("views.physics"), compsciURL=url_for("views.compsci"))

@views.route("/math", methods=["GET","POST"])
def math():
    if request.method == "GET":
        return render_template("math.html")

@views.route("/physics", methods=["GET","POST"])
def physics():
    if request.method == "GET":
        return render_template("physics.html")

@views.route("/compsci", methods=["GET","POST"])
def compsci():
    if request.method == "GET":
        return render_template("compsci.html")