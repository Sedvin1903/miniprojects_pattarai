# Delete data records from the table

from ebbill_schema  import Eb_bill,sessionmaker,engine,or_

Session = sessionmaker(bind=engine)
session = Session()

id = int(input("Enter Customer ID to be deleted : "))
name = input("Enter Customer Name to be deleted : ")

bill  = session.query(Eb_bill).filter((Eb_bill.cid == id )and(Eb_bill.cname == name)).first()

session.delete(bill)
session.commit()

bills = session.query(Eb_bill)
print("\n Updated Table \n")
for bill in bills:
    print(bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 