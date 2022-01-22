# Read data records from the table

from ebbill_schema  import Eb_bill,sessionmaker,engine,or_

Session = sessionmaker(bind=engine)
session = Session()

def display_table():
    bills = session.query(Eb_bill)
    for bill in bills: 
            print(bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 

def count_records():
    bill_C = session.query(Eb_bill).count()
    print("Total No: of records in ",Eb_bill.__tablename__,"is : ",bill_C)
    #bills = session.query(Eb_bill)
    # for bill in bills:
    #    # print('ID','Name','Age','Amount','Bill-date',sep="-----") 
    #     print(bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 

def search_table():
    bills = session.query(Eb_bill)
    print("********************************")
    print("            SEARCH RECORD       ")
    print('1. Customer ID','2. Customer Name',sep='\n')
    print("********************************")
    c= input("Enter your Choice : ")
    if c == '1':
        id = int(input("Enter Customer ID: "))
        bills = session.query(Eb_bill).filter(or_(Eb_bill.cid==id))
        for bill in bills:
            print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 
    if c == '2':
        name = input("Enter Customer Name: ")
        bills = session.query(Eb_bill).filter(or_(Eb_bill.cname==name))
        for bill in bills:
            print('\n',bill.cid,bill.cname,bill.cage,bill.cbillamt,bill.cbilldate,sep=" - ") 
    

print("********************************")
print("         SEARCH OPERATION       ")
print("********************************")
print("1. Display table")
print("2. Search record ")
print("3. Count of records in the table")

c= input("Enter your Choice : ")

if c == '1':
    display_table()
if c == '2':
    search_table()
if c == '3':
    count_records()
    





