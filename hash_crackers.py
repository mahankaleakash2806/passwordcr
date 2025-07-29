import hashlib
import bcrypt
from argon2 import PasswordHasher
from passlib.hash import pbkdf2_sha256

ph = PasswordHasher()

def crack_md5(target_hash, wordlist):
    for password in wordlist:
        if hashlib.md5(password.encode()).hexdigest() == target_hash:
            return password
    return None

def crack_sha1(target_hash, wordlist):
    for password in wordlist:
        if hashlib.sha1(password.encode()).hexdigest() == target_hash:
            return password
    return None

def crack_sha256(target_hash, wordlist):
    for password in wordlist:
        if hashlib.sha256(password.encode()).hexdigest() == target_hash:
            return password
    return None

def crack_bcrypt(target_hash, wordlist):
    for password in wordlist:
        if bcrypt.checkpw(password.encode(), target_hash.encode()):
            return password
    return None

def crack_argon2(target_hash, wordlist):
    for password in wordlist:
        try:
            ph.verify(target_hash, password)
            return password
        except:
            continue
    return None

def crack_pbkdf2(target_hash, wordlist):
    for password in wordlist:
        if pbkdf2_sha256.verify(password, target_hash):
            return password
    return None
