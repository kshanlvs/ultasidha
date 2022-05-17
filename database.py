from click import password_option
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#database connection
DB_URL = "mysql+mysqlconnector://root:Nashikkumar$1@localhost:3306/kpdatabase"

engine = create_engine(DB_URL)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)
