#!/usr/bin/env python3
""" Module of API auth management
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """Class responsible for Auth management.
    """
    def require_auth(self, path:str, excluded_paths: List[str]) -> bool:
       """Checks if a path requires authentication.
       """
       if path is not None and excluded_paths is not None:
            return False

    def authorization_header(self, request=None) -> str:
        """Gets auth header from the request
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        
        return None
