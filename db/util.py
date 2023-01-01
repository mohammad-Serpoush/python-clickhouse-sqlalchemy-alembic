from dotenv import load_dotenv
import os


def get_db_url():
    load_dotenv()
    DB_ENGINE = "clickhouse+native"
    DB_NAME = os.getenv("CLICKHOUSE_DB")
    DB_HOST = os.getenv("CLICKHOUSE_HOST")
    DB_PORT = os.getenv("CLICKHOUSE_NATIVE_PORT")
    DB_USER = os.getenv("CLICKHOUSE_USER")
    DB_PASS = os.getenv("CLICKHOUSE_PASSWORD")
    return f"{DB_ENGINE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
