# Update data in the table

from ebbill_schema  import Eb_bill,sessionmaker,engine


Session = sessionmaker(bind=engine)
session = Session()

def update_Name():
    name = input("Enter Customer Name to be changed : ")
    bill  = session.query(Eb_bill).filter((Eb_bill.cname == name)).first()
    uname = input("Enter Correct Customer Name: ")
    bill.cname = uname
    session.commit()
    print("\n Updated Record \n")
    print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 
  

def update_ID():
    id = int(input("Enter Customer ID to be changed : "))
    bill  = session.query(Eb_bill).filter((Eb_bill.cid == id)).first()
    uid = int(input("Enter Correct Customer ID: "))
    bill.cid = uid
    session.commit()
    print("\n Updated Record \n")
    print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 
    

def update_Age():
    id = int(input("Enter Customer ID for whom age to be changed : "))
    uage = int(input("Enter Correct Customer Age: "))
    bill  = session.query(Eb_bill).filter((Eb_bill.cid == id)).first()
    bill.cage = uage 
    session.commit()
    print("\n Updated Record \n")
    print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 

def update_Bill():
    id = input("Enter Customer ID for whom billamount to be changed : ")
    uamt = float(input("Enter Correct bill amount: "))
    bill  = session.query(Eb_bill).filter((Eb_bill.cid == id)).first()
    bill.cbillamt = uamt
    session.commit()
    print("\n Updated Record \n")
    print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 


print("********************************")
print("         UPDATE OPERATION       ")
print("********************************")
print("1. Customer ID ","2. Customer Name ","3. Customer age ","4. Customer billamt ",sep='\n')

c= input("Enter your Choice : ")

if c == '1':
    update_ID()
if c == '2':
    update_Name()
if c == '3':
    update_Age()
if c == '4':
    update_Bill()

print("\n Updated Table \n")
   #print('ID','Name','Age','Amount','Bill-date',sep="-----") 
bills  = session.query(Eb_bill)
for b in bills:
    print(b.cid,b.cname,b.cage,b.cbillamt,b.cbilldate,sep=" - ") 