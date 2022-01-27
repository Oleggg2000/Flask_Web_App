from datetime import datetime
from flask_package import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    img_profile = db.Column(db.String(20), nullable=False, default="default_img.jpg")
    password = db.Column(db.String(60), nullable=False)

    cart = db.relationship("Product", backref="customer", lazy=True)

    def __repr__(self):
        return f"User('{self.login}', '{self.email}', '{self.img_profile}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Product('{self.title}', '{self.date_created}')"