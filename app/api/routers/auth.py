from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core import models, schemas
from app.core.security import create_access_token, verify_password, get_password_hash
from app.core.db import get_db

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"msg": "User created successfully"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # Sua lógica de login
    pass

