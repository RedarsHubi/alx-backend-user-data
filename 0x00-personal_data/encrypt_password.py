#!/usr/bin/env python3
"""
Module for encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """salted password"""
    salt = bcrypt.gensalt()

    hashed_pass = bcrypt.hashpw(password.encode(), salt)

    return hashed_pass
