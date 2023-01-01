from sqlalchemy import create_engine, MetaData

from clickhouse_sqlalchemy import make_session

from db.util import get_db_url


URI = get_db_url()

engine = create_engine(URI)
session = make_session(engine)
metadata = MetaData(bind=engine)
