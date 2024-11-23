from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()


class Products(Base):
    __tablename__='Products'
    id=Column(Integer,primary_key=True)
    Name=Column(String(255),nullable=False)
    Price=Column(String,nullable=False)
    quantity=Column(String,nullable=False)
