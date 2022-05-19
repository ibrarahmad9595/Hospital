from model.Person import Person
from model.Doctor import Doctor

class Hospital:
    def __init__(self):
        self.person_dic = {}
        self.doctor_dic = {}

    def addPerson(self, name, surname, personId):
        person = Person(name,surname,personId)
        if personId not in self.person_dic:
            self.person_dic[personId] = person

    def addDoctor(self, name, surname, personId, doctorId):
        doctor = Doctor(name, surname, personId, doctorId)
        if personId in self.person_dic:
            if doctorId not in self.doctor_dic:
                self.doctor_dic[doctorId] = doctor

    ## Person not present exception
    def getPerson(self, personId):
        check_person = None
        for person_id in self.person_dic:
            if personId == person_id:
                check_person = person_id
                return self.person_dic[check_person]
        if not check_person:
            raise Exception ("Person not present")

    ## Doctor not present exception
    def getDoctor(self, doctorId):
        check_doctor = None
        for doctor_id in self.doctor_dic:
            if doctorId == doctor_id:
                check_doctor = doctor_id
                return self.doctor_dic[check_doctor]
        if not check_doctor:
            raise Exception ("Doctor not present")

    def assignDoctor(self, doctorId, personId):
        for person in self.person_dic:
            if personId == person:
                for doctor in self.doctor_dic:
                    if doctorId == doctor:
                        self.person_dic[person].setDoctor(doctor)
                        self.doctor_dic[doctor].addPatient(self.person_dic[person])
                        break