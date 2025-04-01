from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    datetime = db.Column(db.DateTime, nullable=False)
    diet = db.Column(db.String(80), nullable=False)