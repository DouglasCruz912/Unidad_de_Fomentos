from datetime import datetime
from .database import Base
from sqlalchemy import Column,Integer,String,Float,DateTime



class Uf(Base):
    __tablename__ = "unidad"
    id = Column(Integer,primary_key=True,autoincrement=True)
    date = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    unidad_de_fomento = Column(Float)
    