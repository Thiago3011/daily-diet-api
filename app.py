from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:5000/daily-diet'

db.init_app(app)

@app.route("/", methods=['GET'])
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)
