
from database import Base
from sqlalchemy import Column,Integer,String


class Users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True)
    password =Column(String(100))


class Kishan(Base):
    __tablename__="kishan"
    id=Column(Integer,primary_key=True,index=True)