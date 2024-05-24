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