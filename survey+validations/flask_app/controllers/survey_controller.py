from flask import render_template, request, redirect, session
from flask_app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']
    session['color'] = request.form['color']
    session['transport'] = request.form['transport']
    return redirect ("/new")

@app.route('/new')
def new_page():
    return render_template ("new.html", color = session['color'])
# @app.route('/destroy')
# def increase():
#     session.clear()
#     return redirect("/")


