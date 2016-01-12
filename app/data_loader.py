#!/usr/bin/python
from data_config import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from models.master import Master

if __name__ == "__main__":
    Base = declarative_base()
    print (DATABASE_URI)
    engine = create_engine(DATABASE_URI, echo=True)
    Base.metadata.create_all(engine)
    print(Master.__table__)
