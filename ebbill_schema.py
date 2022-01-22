import datetime
from sqlalchemy import create_engine,Column,Integer,BigInteger,String,Float,Date,or_,and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To showcase the SQL Queries done by SQLAlchemy
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


engine = create_engine('mysql://root:FRBros_2021@localhost/crud_alchemy')

Session = sessionmaker(bind=engine)



Base = declarative_base()

class Eb_bill(Base):
    
    __tablename__ ='eb_billg'

    # Column attributes of Table "eb_billg"  in Schema "crud_alchemy"
    cid = Column(BigInteger,primary_key=True)
    cname = Column(String(25))
    cage = Column(Integer)
    cbillamt = Column(Float(10))
    cbilldate = Column(Date)


Base.metadata.create_all(engine)

