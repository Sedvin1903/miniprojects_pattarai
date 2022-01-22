# Create data record in the table

from ebbill_schema  import Eb_bill,sessionmaker,engine
from datetime import date
#from sqlalchemy.orm import sessionmaker


id = int(input("Enter Customer ID: "))
name = input("Enter Customer Name: ")
age = int(input("Enter Customer Age: "))
bilamt = float(input("Enter Customer Bill amount from message : "))
today = date.today()
billdate = today

Session = sessionmaker(bind=engine)
session = Session()

bill1 = Eb_bill(cid=id,cname=name,cage=age,cbillamt=bilamt,cbilldate=billdate ) 

session.add(bill1)

session.commit()