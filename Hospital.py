from model.Person import Person
from model.Doctor import Doctor
class Hospital:
    def __init__(self):
        self.person_list = []
        self.doctor_list = []

    def addPerson(self, name, surname, personId):
        person = Person(name,surname,personId)
        if len(self.person_list) == 0:
            self.person_list.append(person)
        else:
            person_id_list = []
            for per in self.person_list:
                person_id_list.append(per.personId)
            if personId not in person_id_list:
                self.person_list.append(person)

    def addDoctor(self, name, surname, personId, doctorId):
        doctor = Doctor(name, surname, personId, doctorId)
        person_id_list = []
        for per in self.person_list:
            person_id_list.append(per.personId)
            if personId in person_id_list:
                if len(self.doctor_list) == 0:
                    self.doctor_list.append(doctor)
                else:
                    doctor_id_list = []
                    for doct in self.doctor_list:
                        doctor_id_list.append(doct.doctorId)
                    if doctorId not in doctor_id_list:
                        self.doctor_list.append(doctor)

    ## Person not present exception
    def getPerson(self, personId):
        for person in self.person_list:
            if personId == person.personId:
                return person
            else:
                raise Exception ("Person not present")

    ## Doctor not present exception
    def getDoctor(self, doctorId):
        for doctor in self.doctor_list:
            if doctorId == doctor.doctorId:
                return doctor
            else:
                raise Exception ("Doctor not present")

    def assignDoctor(self, doctorId, personId):
        for person in self.person_list:
            if personId == person.personId:
                for doctor in self.doctor_list:
                    if doctorId == doctor.doctorId:
                        if len(doctor.patient_list)==0:
                            person.setDoctor(doctor)
                            doctor.addPatient(person)
                        else:
                            check_pat = []
                            for pat in doctor.patient_list:
                                check_pat.append(pat.personId)
                            if personId not in check_pat:
                                person.setDoctor(doctor)
                                doctor.addPatient(person)
