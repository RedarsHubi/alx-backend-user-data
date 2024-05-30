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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks validity"""
    return bcrypt.checkpw(password.encode(), hashed_password)
