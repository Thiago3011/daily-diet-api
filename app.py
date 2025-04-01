from flask import Flask, request, jsonify
from models.meal import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/daily-diet'

db.init_app(app)

@app.route("/meal", methods=['POST'])
def create_meal():
    data = request.json

    name = data.get("name")
    description = data.get("description", "")
    diet = data.get("diet")
    datetime = data.get("datetime")

    if name and diet and datetime:
        meal = Meal(id=data.get("id"), name=name, description=description, datetime=datetime, diet=diet)
        db.session.add(meal)
        db.session.commit()

        return jsonify({"message": "Refeição cadastrada com sucesso!"})
    
    return jsonify({"message": "Dados ausentes"}), 400

@app.route("/meal/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
    data = request.json
    meal = Meal.query.get(meal_id)

    if data and meal:
        meal.name = data.get("name")
        meal.description = data.get("description", meal.description)
        meal.datetime = data.get("datetime")
        meal.diet = data.get("diet")
        db.session.commit()
        
        return jsonify({"message": "Refeição atualizada com sucesso!"})

    return jsonify({"message": "Dados ausentes"}), 400

if __name__ == "__main__":
    app.run(debug=True)
