from dis import dis
from http.client import HTTPException
from os import uname
from typing import List
from unicodedata import name
from fastapi import Depends, FastAPI
from model import Users
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from database import Base, SessionLocal, engine
app = FastAPI()

# this will create tables in database
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserSchema(BaseModel):

    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    password: str

# get method


data = {}


@app.get("/dependu")
def get_dependu(db: Session = Depends(get_db)):

    return {"data": db.query(Users).all()}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    return {"data": db.query(Users).all()}

# create method


@app.post("/users", response_model=UserSchema)
def get_users(user: UserCreateSchema, db: Session = Depends(get_db)):
    u = Users(name=user.name, email=user.email, password=user.password)
    db.add(u)
    db.commit()
    return u

# update method


@app.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        u.name = user.name
        u.email = user.email
        db.add(u)
        db.commit()
        return u
    except:
        return HTTPException(status_code="404", details="user not found")

# delete method


@app.delete("/users/{user_id}", response_class=JSONResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        db.delete(u)
        db.commit()
        return {f"user with id {user_id} has been deleted"}
    except:
        return HTTPException(status_code="404", details="user not found")
