from flask import Blueprint
from controllers.fruits_controller import index, new, create, edit, update, delete, like

fruits_routes = Blueprint('fruits_routes', __name__)

fruits_routes.route('')(index)
fruits_routes.route('/new')(new)
fruits_routes.route('', methods=['POST'])(create)
fruits_routes.route('/<id>/edit')(edit)
fruits_routes.route('/<id>', methods=['POST'])(update)
fruits_routes.route('/<id>/delete', methods=["POST"])(delete)
fruits_routes.route('/<id>/likes', methods=["POST"])(like)