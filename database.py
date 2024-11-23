from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine('mysql+pymysql://FYNDflaskdb:faizal6263@FYNDflaskdb.mysql.pythonanywhere-services.com/FYNDflaskdb$fynd')
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()