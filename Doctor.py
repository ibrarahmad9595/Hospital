from model.Person import Person
#DoctorID
#3454FHHG

class Doctor(Person):
    def __init__(self, name, surname, personId, doctorId):
        self.name = name
        self.surname = surname
        self.personId = personId
        self.doctorId = doctorId
        self.patient_list = []

    def getDoctorId(self):
        return self.doctorId

    def addPatient(self, person):
        check_pat = []
        for pat in self.patient_list:
            check_pat.append(pat.personId)
        if person.personId not in check_pat:
            self.patient_list.append(person)

    def getPatients(self):
        return self.patient_list
