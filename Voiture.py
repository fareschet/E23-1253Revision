# -*- coding: utf-8 -*-
class Voiture:
    def __init__(self, v_marque, v_annee, personne):
        self.marque = v_marque
        self.annee = v_annee
        self.personne = personne

    def afficher_voiture(self):
        print("La voiture de marque " + str(self.marque) + " avec l'année " + str(
            self.annee) + " appartient à la personne:\n nom:" + str(self.personne.nom) + "\n prenom: " + str(self.personne.prenom))
class Personne:
    def __init__(self, p_nom, p_prenom):
        self.nom = p_nom
        self.prenom = p_prenom

p1 = Personne("Chettouh", "Fares")
p2 = Personne("Mickeal", "jackson")
v1 = Voiture("Mercedes", "2019",p2)
v2 = Voiture("Mazda", "2023",p1)
v1.afficher_voiture()
v2.afficher_voiture()