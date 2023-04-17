# import psycopg2

# conn = psycopg2.connect(
#     database='password-manager', user='postgres', password='y7pEFwg3ZEgYpKA7qTVF', host='127.0.0.1', port= '5432'
# )
# cursor = conn.cursor()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:y7pEFwg3ZEgYpKA7qTVF@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()