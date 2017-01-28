from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

DB_URI = getenv('DB_URI')
if not DB_URI:
    raise Exception('DB_URI should be specified')

engine = create_engine(DB_URI, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
base = declarative_base()
base.query = db_session.query_property()


def init_db():
    base.metadata.create_all(bind=engine)
