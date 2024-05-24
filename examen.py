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
