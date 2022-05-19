
#Nome	    Cognome	    Codice Fiscale
#Giovanni	Rossi	    RSSGNN33B30F316I
#Giuseppe	Verdi	    VRDGPP76F09B666I

class Person:
    def __init__(self, name, surname, personId):
        self.name = name
        self.surname = surname
        self.personId = personId


    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getId(self):
        return self.personId

    def setDoctor(self, doctor):
        self.doctor = doctor

    def getDoctor(self):
        return self.doctor
