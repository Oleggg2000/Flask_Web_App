from flask import Flask, url_for, render_template

app = Flask(__name__)

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


@app.route("/login")
def loginIn_page():
    return render_template("login.html", title="Login In")


@app.route("/singup")
def singUp_page():
    return None


@app.route("/products")
def products_page():
    return None


@app.route("/cart")
def cart_page():
    return None


if __name__ == "__main__":
    app.run(debug=True)