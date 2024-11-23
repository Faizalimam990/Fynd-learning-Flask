from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base

Database_URL='sqlite:///database.db'
engine=create_engine(Database_URL)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()