from flask import Blueprint, render_template, request, flash, redirect, url_for
import os, random


views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html")

@views.route("/math/<arg>", methods=["GET","POST"])
def math(arg):
    if arg == "get":
        return render_template("math.html")
    
    params = arg.split("_")

    directory = "website/static/math"
    if params[0] == "shuffle":
        ext = random.choice(["further","single"])
        directory += f"/{ext}"
        ext = random.choice(["pure","stats", "mech"])
        directory += f"/{ext}"

    elif params[1] == "shuffle":
        ext = random.choice(["pure","stats","mech"])
        directory += f"/{params[0]}/{ext}"

    else:
        directory += f"/{params[0]}/{params[1]}"

    contents = os.listdir(directory)
    try:
        index = random.randint(1, len(contents)//2)
    except:
        return "directory empty"
    question = f"{directory}/{index}q.png"
    question = question[8:]
    answer = f"{directory}/{index}a.png"
    answer = answer[8:]
    print(question, answer)
    return render_template("QA.html", question=question, answer=answer)

@views.route("/physics/<arg>", methods=["GET","POST"])
def physics(arg):
    if arg == "get":
        return render_template("physics.html")
    
    params = arg.split("_")

    topics = {"paper1":["measurementsAndTheirErrors", "particlesAndRadiation", "waves", "mechAndMaterials", "electricity"],
                   "paper2":["thermal", "fields", "nuclear"],
                   "paper3":["practicalSkills","turningPoints"]}

    directory = "website/static/physics"
    if params[0] == "shuffle":
        ext = random.choice(["paper1","paper2", "paper3"])
        directory += f"/{ext}"
        
        ext = random.choice(topics[ext])
        directory += f"/{ext}"

    elif params[1] == "shuffle":
        ext = random.choice(topics[params[0]])
        directory += f"/{params[0]}/{ext}"

    else:
        directory += f"/{params[0]}/{params[1]}"

    contents = os.listdir(directory)
    try:
        index = random.randint(1, len(contents)//2)
    except:
        return "directory empty"
    question = f"{directory}/{index}q.png"
    question = question[8:]
    answer = f"{directory}/{index}a.png"
    answer = answer[8:]
    
    return render_template("QA.html", question=question, answer=answer)

@views.route("/compsci", methods=["GET","POST"])
def compsci():
    if request.method == "GET":
        return render_template("compsci.html")