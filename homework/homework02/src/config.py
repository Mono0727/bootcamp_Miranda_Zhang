import os
from dotenv import load_dotenv


def load_env():
    load_dotenv("../../../.env")


def get_key(key_name):
    value = os.getenv(key_name)

    if value is None:
        raise ValueError(f"Environment variable '{key_name}' not found.")

    return value