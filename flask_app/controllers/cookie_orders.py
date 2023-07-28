from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie_order import Cookie_order 
#GET ROUTES
@app.route("/")
@app.route("/cookies")
def index():
    print("In index page route")
    all_orders = Cookie_order.get_all()
    return render_template("cookies.html", orders = all_orders)

@app.route("/cookies/new")
def new_page():
    print("In new page route")
    return render_template("new_order.html")

@app.route("/cookies/edit/<order_id>")
def edit_page(order_id):
    cookie_order = Cookie_order.get_one(order_id)
    print("In edit route with id", order_id)
    return render_template("edit_order.html", cookie_order = cookie_order)

# POST (ACTION) ROUTES
@app.route("/cookies/create", methods=["POST"])
def create_order():
    print("In create POST route")
    if Cookie_order.validate_cookie_order(request.form):
        Cookie_order.save(request.form)
        return redirect("/cookies")
    return redirect("/cookies/new")

@app.route("/cookies/update", methods=["POST"])
def update_order():
    print("In update POST route")
    print(request.form)
    if Cookie_order.validate_cookie_order(request.form):
        Cookie_order.edit(request.form)
        return redirect("/cookies")
    return redirect("/cookies/edit/{request.form['id']}")

