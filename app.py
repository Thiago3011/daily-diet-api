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

    if name and diet:
        meal = Meal(id=data.get("id"), name=name, description=description, created_at=data.get("created_at"), diet=diet)
        db.session.add(meal)
        db.session.commit()

        return jsonify({"message": "Refeição cadastrada com sucesso!"})
    
    return jsonify({"message": "Dados ausentes"}), 400

if __name__ == "__main__":
    app.run(debug=True)
