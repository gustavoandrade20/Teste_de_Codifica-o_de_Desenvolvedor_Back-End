from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models, schemas, session

router = APIRouter(prefix="/clients")

@router.get("/")
def list_clients(db: Session = Depends(session.get_db)):
    return db.query(models.Client).all()

@router.post("/")
def create_client(client: schemas.ClientCreate, db: Session = Depends(session.get_db)):
    db.add(models.Client(**client.dict()))
    db.commit()
    return {"msg": "Client created"}
