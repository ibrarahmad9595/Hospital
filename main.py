from model.Hospital import Hospital
from model.Person import Person
from model.Doctor import Doctor

hospital = Hospital()
hospital.addPerson("Mike","Jhonson","EF122")
hospital.addPerson("Franco","Italian","EF127")
hospital.addPerson("Conti","Luana","EF123")
hospital.addPerson("Conti","laura","EF123")
hospital.addPerson("Maria","Mariani","EF124")
hospital.addDoctor("Conti","Luana","EF123","D01")
hospital.addDoctor("Maria","Mariani","EF124","D02")
hospital.getPerson("EF122")
hospital.getDoctor("D02")
hospital.assignDoctor("D01", "EF122")
hospital.assignDoctor("D02", "EF123")
hospital.assignDoctor("D02", "EF127")
person = Person("Conti","Luana","EF123")
person.getName()
person.getId()
person.setDoctor([{'name':"Conti", 'surname':"Luana",'personId':"EF123",'doctorId':"D01"}])
person.getDoctor()

pers = Person("Conti","Luana","EF123")
doctor = Doctor("Conti","Luana","EF123","D01")
doctor.addPatient(pers)
print("abc")