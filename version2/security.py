from werkzeug.security import safe_str_cmp
from resources.user import UserModel

# create authenticate & idetity fuctions used in JWT 
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# return the ID of the user
def identity(payload):  # payload is the content of the JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    
