"""INTENTIONALLY VULNERABLE training examples. Never deploy this file."""
import hashlib
import os
import pickle
import sqlite3
import subprocess
import yaml
import requests


password = "SuperSecret123!"


def sql_injection(cursor):
    user_id = input("Enter user ID: ")
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)


def sql_injection_percent(cursor):
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)


def sql_injection_format(cursor):
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = '{}'".format(user_id)
    cursor.execute(query)


def command_injection(user_input):
    subprocess.run("ping -c 1 " + user_input, shell=True)
    os.system("echo " + user_input)


def unsafe_deserialization(blob):
    return pickle.loads(blob)


def weak_crypto(value):
    return hashlib.md5(value.encode()).hexdigest()


def weak_crypto_sha1(value):
    return hashlib.sha1(value.encode()).hexdigest()


def unsafe_tls(url):
    return requests.get(url, verify=False, timeout=5)


def unsafe_yaml(document):
    return yaml.load(document)


def dynamic_code_execution(expression):
    eval(expression)


def dynamic_code_execution_exec(code):
    exec(code)
