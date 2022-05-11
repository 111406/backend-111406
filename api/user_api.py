from flask import Blueprint, request
from service.user_service import signup_service, search_service

user_route = Blueprint('user_route', __name__)

@user_route.route("/api/user", methods=['GET'])
def search():
    return search_service()