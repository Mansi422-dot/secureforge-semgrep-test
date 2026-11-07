"""Safe examples intended not to trigger SecureForge custom rules."""

import hashlib
import sqlite3
import subprocess
import yaml
import json


def safe_query(connection: sqlite3.Connection, user_id: str):
    return connection.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,),
    )


def safe_digest(value: bytes):
    return hashlib.sha256(value).hexdigest()


def safe_command(host: str):
    # Argument list, no shell=True.
    return subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        check=False,
    )


def safe_yaml(document: str):
    return yaml.safe_load(document)


def safe_deserialization(document: str):
    # JSON does not deserialize arbitrary Python objects.
    return json.loads(document)


def safe_password_configuration():
    # Read secrets from environment/configuration rather than hardcoding.
    import os
    return os.environ.get("APP_PASSWORD")
