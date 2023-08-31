from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "People"
    idno = Column(Integer, primary_key=True,autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(CHAR)
    age = Column(Integer)
    
    def __init__(self, first, last, gender, age):
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
        
    def __repr__(self):
        return f"({self.idno}) {self.firstname} {self.lastname} ({self.gender} {self.age})"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

p1 = Person("Mike", "Doe", "M", 40 )
p2 = Person("Jane", "Doe", "F", 35)
p3=Person("Wilson","Kinyua", "M",13)
p4=Person("Albert","Byrone","M",25)
p5=Person("Collins","Kipkorir","M",23)
p6=Person("Vincent","Koech","M",10)


session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)
session.add(p6)
session.commit()
age_threshold=10
new_firstname="Maluki"
record_to_update=session.query(Person).filter_by (age=age_threshold).all()
if record_to_update:
    for record in record_to_update:
        record.firstname=new_firstname
        session.commit()
    print("The name have been updated")
else:
    print("No records found for the given age")
record_to_delete=session.query(Person).filter(Person.age>age_threshold).all()
if record_to_delete:
    for record in record_to_delete:
        session.delete(record)
        session.commit()
    print("The record have been deleted")  
else:
    print("No records found with ages greater than", age_threshold)