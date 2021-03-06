from flask import Blueprint, request, make_response
from service.user_service import signup_service, search_service

user_route = Blueprint('user_route', __name__)
root_path = "/api/user"

@user_route.route(f"{root_path}/signup", methods=['POST'])
def signup():
    data = request.get_json()
    message = ""
    status = 200
    try:
        signup_service(data)
        message = "註冊成功"
    except Exception as e:
        message = str(e)
        status = 500
    response = make_response({"message": message}, status)
    return response

@user_route.route(root_path, methods=['GET'])
def search():
    result = []
    message = ""
    status = 200
    try:
        result = search_service()
        message = "查詢成功"
    except Exception as e:
        message = str(e)
        status = 500
    response = make_response({"message": message, "data": result}, status)
    return response