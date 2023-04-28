from datetime import datetime
from fastapi import FastAPI,Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import Base, SessionLocal,engine, get_db
from app.db import models



app = FastAPI()

     

@app.get("/")
async def saludos():
    return 'saludos'

@app.get("/get-uf")
async def consulta_de_unidad_de_fomentos(db:Session = Depends(get_db)):
    data=db.query(models.Uf).all()
    return data



@app.get("/get-uf-by-date",status_code=200)
async def get_uf_by_date(date:datetime, db:Session = Depends(get_db)):
    data=db.query(models.Uf).filter_by(date=date).one_or_none()
    if data == None:
        raise HTTPException(status_code=400, detail="Error: La fecha que ingreso no existe, ingrese una fecha validad")
    else:
        return { "uf": data.unidad_de_fomento }



