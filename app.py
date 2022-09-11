from flask import Flask
from routes.users import users
from routes.aids import aids
from config.config import DATABASE_CONNECTION_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return {'status': 'API running'}

SQLAlchemy(app)

app.register_blueprint(users)
app.register_blueprint(aids)

if __name__ == '__main__':
    app.run(debug = True)   