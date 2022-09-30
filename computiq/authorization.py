from django.contrib.auth import get_user_model
from ninja.security import HttpBearer
from jose import jwt, JWTError

from config import settings

User = get_user_model()


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20ifQ.X9-RqWLql-9n6NrkFVjXETHv2BRcVBaCXiQmXK3Nwws

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            user_username = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms='HS256')
        except JWTError:
            return {'token': 'unauthorized'}

        if user_username:
            return 200


def create_token_for_user(user):
    token = jwt.encode({'username': str(user.username)}, key=settings.SECRET_KEY, algorithm='HS256')
    return str(token)
