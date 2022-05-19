from model.Person import Person
#DoctorID
#3454FHHG

class Doctor(Person):
    def __init__(self, name, surname, personId, doctorId):
        super(Doctor, self).__init__(name, surname, personId)
        self.doctorId = doctorId
        self.patient_dic= {}

    def getDoctorId(self):
        return self.doctorId

    def addPatient(self, person):
        if person not in self.patient_dic:
            self.patient_dic[person.personId] = person

    def getPatients(self):
        return self.patient_dic
