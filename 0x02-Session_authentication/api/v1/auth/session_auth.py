#!/usr/bin/env python3
""" Module of Session Auth"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Auth class """
    user_id_by_session_id = {}

    def __init__(self):
        '''init'''
        pass

    def create_session(self, user_id: str = None) -> str:
        """creates sessions with id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user id based on session id"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
