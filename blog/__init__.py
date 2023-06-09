# intializtation file

from flask import Flask
from blog.config import project_config
from blog.models import db, Posts
from flask_migrate import Migrate



def create_app(config_name):
    app=Flask(__name__)
    app_state = project_config[config_name]
    app.config.from_object(app_state)
    
    # db
    app.config["SQLALCHEMY_DATABASE_URI"] = app_state.SQLALCHEMY_DATABASE_URI
    
    db.init_app(app)
    
    # blueprint for route
    from blog.post.postBlueprints import post_blueprint
    app.register_blueprint(post_blueprint)
    
    # add migration
    migrate = Migrate(app, db, render_as_batch=True)
    
    
    return app

