from flask import Blueprint

post_blueprint = Blueprint('blog', __name__, url_prefix='/posts')

