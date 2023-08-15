from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "databse.db"

#*initialze application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sksjdksdjklsdjsldfeetewsvnh'
    #*this is to tell flask where the db will be stored
    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    #*load the models from db
    from .models import User, Note
    
    with app.app_context():
        try:
            print("creating db")
            db.create_all()
        except Exception as e:
            print(f"An error occurred while creating the database: {e}")
    
    return app

#*this function checks if db exists already, if not it will create a db
# def create_database(app):
#     #* website is the name of the folder
#     if not path.exists('website/' + DB_NAME):
#         with app.app_context():
#             db.create_all(app)
#             print('Created Database!')