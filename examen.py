from abc import ABC 
""" Classe Abstraite"""
class Employe(ABC):
    """Initialise le nom et la specialite"""
    def __init__(self, nom=None, specialite=None):
        self.__nom = nom
        self.__specialite = specialite
    """ Creation des methodes """
    def afficher_infos(self):
        print(f"Nom: {self.__nom}\nSpecialite: {self.__specialite}")
    def action(self):
        print("Soinger les malades à l'hopital")


""" Heritage de la classe Medecin """
class Medecin(Employe):
    def __init__(self, nom, specialite):
        self.__nom = nom
        self.__specialite = specialite
    """ Le get et  le set pour acceder aux methodes prives """
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom = nom

    def getspecialite(self):
        return self.__specialite
    def setspecialite(self,specialite):
        self.__specialite=specialite
    """ Creation des methodes """
    def afficher_infos(self):
        print(f"Nom: {self.__nom}\nSpecialite: {self.__specialite}")
    """ Polymorphisme """
    def action(self):
        print("Le médecin examine le patient.")


    """ Heritage de la classe, l'encapsulation et le polymorphisme """
class Pediatre(Employe):
    def __init__(self, nom, specialite, service):
        self.__nom = nom
        self.__specialite = specialite
        self.service = service
    """ Le get et  le set pour acceder aux methodes prives """
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom = nom
    def getspecialite(self):
        return self.__specialite
    def setspecialite(self,specialite):
        self.__specialite=specialite
    """ Creation des methodes """
    # Surcharge de la méthode afficher_infos pour inclure le service
    def afficher_infos(self):
        print(f"Nom: {self.__nom}\nSpecialite: {self.__specialite}\nService: {self.service}")
    """ Polymorphisme """
    def action(self):
        print("Le pédiatre prescrit un vaccin.")
class Cardiologue(Employe):
    def __init__(self, nom, specialite, hopital):
        self.__nom = nom
        self.__specialite = specialite
        self.hopital = hopital
    """ Le get et  le set pour acceder aux methodes prives """
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom = nom
    def getspecialite(self):
        return self.__specialite
    def setspecialite(self,specialite):
        self.__specialite=specialite
    """ Creation des methodes """
    # Surcharge de la méthode afficher_infos pour inclure l'hôpital
    def afficher_infos(self):
        print(f"Nom: {self.__nom}\nSpecialite: {self.__specialite}\nHopital: {self.hopital}")
    """ Polymorphisme """
    def action(self):
        print("Le cardiologue effectue une échographie.")

"""Instanciation des classes """
print("Infos sur le medecin")
setnom=input("Entrer le nom du medecin: ")
setspecialite=input("Entrer son specialite: ")
medecin_generaliste = Medecin(setnom, setspecialite)
medecin_generaliste.afficher_infos()
medecin_generaliste.action()

print("Infos sur le Pediatre")
setnom=input("Entrer le nom du pediatre: ")
setspecialite=input("Entrer son specialite: ")
service=input("Entrer son service: ")
pediatre_hopital = Pediatre(setnom, setspecialite, service)
pediatre_hopital.afficher_infos()
pediatre_hopital.action()

print("Infos sur le Cardiologue")
setnom=input("Entrer le nom du cardiologue: ")
setspecialite=input("Entrer son specialite: ")
hopital=input("Entrer son Hopital: ")
cardiologue_prive = Cardiologue(setnom, setspecialite, hopital)
cardiologue_prive.afficher_infos()
cardiologue_prive.action()