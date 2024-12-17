from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# this is for raw sql psycopg
import psycopg2
# to give you the column name instead of just the values
from psycopg2.extras import RealDictCursor 
import time


from .config import settings

# to connect our ORM to postgress in our app

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)


# This creates a session factory that you can use to interact with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the base class for all your ORM models.
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# when using psycopg2 to connect app and postgress using raw SQL (this is not fr ORM sqlqlchemy o)
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='testing123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connection was a success")
#         break
#     except Exception as error:
#         print("was not successful")
#         print('Error:, ', error)
#         time.sleep(2)







# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'




