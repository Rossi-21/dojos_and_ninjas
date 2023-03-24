from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo # import class from flask_app.modles.user
from flask_app.models.ninja import Ninja
#app.route goes in this file

@app.route('/dojos')          
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos) 

@app.route('/create_dojo', methods=["POST"])
def create():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route('/dojos/<int:id>/')
def show(id):
    data = {
        "id" : id
    }  
    return render_template("show.html", dojo=Dojo.get_dojo_with_ninjas(data))


