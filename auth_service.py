import hashlib
import os

users = {}


def hash_password(password, salt=None):
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt, digest


def register_user(email, password):
    if email in users:
        return {"status": 409, "error": "An account with this email already exists"}
    if len(password) < 12:
        return {"status": 400, "error": "Password must be at least 12 characters"}
    salt, digest = hash_password(password)
    users[email] = {"salt": salt, "hash": digest, "verified": False}
    return {"status": 201, "state": "pending_verification"}