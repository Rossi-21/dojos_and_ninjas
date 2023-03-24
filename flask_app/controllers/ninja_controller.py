from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo #import class from flask_app.modles 
from flask_app.models.ninja import Ninja
#app.route goes in this file

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
        data = {
            "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "age" : request.form["age"],
            "dojo_id" : request.form["dojo_id"]
        }
        Ninja.save(data)
        return redirect(f'/dojos/{request.form["dojo_id"]}')

@app.route('/dojos/delete_ninja/<int:id>/')
def delete_user(id):
    data = {
        "id" : id
    }
    Ninja.delete(data)
    return redirect(request.referrer)

@app.route('/ninjas/edit/<int:id>')
def update_ninja(id):
    data = {
        "id": id
    }
    return render_template("edit.html", ninja=Ninja.get_one(data))

@app.route('/update_ninja', methods=["POST"])
def update_user():
    Ninja.update(request.form)
    return redirect('/dojos')
