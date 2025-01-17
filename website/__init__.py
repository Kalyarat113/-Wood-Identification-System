from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
 

db = SQLAlchemy()
DB_NAME = 'wood-identification-project.db'

UPLOAD_FOLDER = 'wood-project-mainstatic/images'
 
 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KeY'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['RECAPTCHA_SITE_KEY'] = '6Lf07ugpAAAAAGawO9tMxqItiZBQGPOZJwsGs1IW'
    app.config['RECAPTCHA_SECRET_KEY'] = '6Lf07ugpAAAAAD1BnoNvN5RnK5I65rqqpJ_Cfhku'
    app.config['VERIFY_URL'] = "https://www.google.com/recaptcha/api/siteverify"


    db.init_app(app)


    from .views import views_blueprint
    from .auth import auth_blueprint
    from .manages import manage_blueprint

    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(manage_blueprint, url_prefix='/')

    from .models import User


    # create_database(app)
    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth_blueprint.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

        
    return app


def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all(app=app)
        print('Created Database!!!')

