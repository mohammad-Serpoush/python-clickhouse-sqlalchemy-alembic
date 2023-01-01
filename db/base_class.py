from clickhouse_sqlalchemy import get_declarative_base

from db.database import metadata


Base = get_declarative_base(metadata=metadata)
