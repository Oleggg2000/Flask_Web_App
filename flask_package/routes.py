from flask import render_template, redirect, flash, url_for
from flask_package import app
from flask_package.forms import RegistrationForm, LoginForm

products = [
    {
        'title': 'Product 1',
        'content': 'First product content',
        'date_created': 'January 25, 2021'
    },
    {
        'title': 'Product 2',
        'content': 'Second product content',
        'date_created': 'January 28, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html", title="Home", products=products)


@app.route("/login", methods=["GET", "POST"])
def loginIn_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "lol@mail.ru" and form.password.data == "12345":
            flash(f"You've been logged in!", "success")
            return redirect("home")
        else:
            flash(f"Error. Check login or password!", "danger")
    return render_template("login.html", title="Login In", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signUp_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account was created for {form.email.data}!", "success")
        return redirect("home")
    return render_template("registration.html", title="Registration", form=form)


@app.route("/products")
def products_page():
    return None


@app.route("/cart")
def cart_page():
    return None