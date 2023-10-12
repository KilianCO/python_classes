# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:30:47 2022

@author: p2006902
"""

## ==== La classe Voiture ====
class Voiture():
    
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix
        
    
    def compare(self, car):
        if self.marque == car.marque and self.prix == car.prix:
            return True
        else:
            return False
    
    def affiche(self):
        print(self.marque, self.prix)
        
        
## ==== La classe voiture occasion ====
class VoitureOccasion(Voiture):
    def __init__(self, marque, prix, km):
        super().__init__(marque, prix)
        self.km = km
    
    def compare(self, car):
        if self.marque == car.marque and self.prix == car.prix and self.km == car.km :
            return True
        else:
            return False
    
    def affiche(self):
        print(self.marque, self.prix, self.km)
        

## ==== La classe garage ====
class Garage():
    def __init__(self, liste):
        self.liste = liste
    
    
    def affiche(self):
        for i in range(len(self.liste)):
            self.liste[i].affiche()
            
    def doublons(self):
        liste1 = []
        for i in self.liste:
            if i not in liste1:
                liste1 = liste1 + [i]
        self.liste = liste1      
    
    def ajoute(self, voiture):
        self.liste.append(voiture)        
    

## ==== Question 5 ==== 
# On a pas besoin d'ajouter une méthode qui ajoute une VoitureOccasion
# Car on a déjà une méhode pour ajouter une Voiture
# Et la VoitureOccasion est par héritage une Voiture

     
    def cptMarques(self):
        listeMarques = []
        nb = []
        for i in range(len(self.liste)):
            if self.liste[i].marque not in listeMarques:
                listeMarques = listeMarques + [self.liste[i].marque]
                nb = nb + [1]
            else:
                indice = listeMarques.index(self.liste[i].marque)
                nb[indice] += 1
        return listeMarques, nb


    
## ==== La classe principale ====
def Principale():
    print("Création et affichage d'une voiture")
    car1 = Voiture("Mercedez", "10")
    car1.affiche()
    
    
    print("Création et affichage d'une seconde voiture")
    car2 = Voiture("Audi", "40")
    car2.affiche()
    
    
    print("Comparaison des deux voitures")
    print(car2.compare(car1)) # renvoie False
    
    
    print("Création et affichage d'une voiture d'occasion")
    car3 = VoitureOccasion("Citroen", "5","250000")
    car3.affiche()
    
    
    print("Création et affichage d'une seconde voiture d'occasion")
    car4 = VoitureOccasion("Twingo", "1","500000")
    car4.affiche()
    
    
    print("Comparaison des deux voitures d'occasion")
    print(car3.compare(car4)) # renvoie False
    print(car3.compare(car3)) # renvoie True

    print("Comparaison entre une voiture et une voiture occasion")
    print(car1.compare(car3)) # renvoie False
    print(car2.compare(car3)) # renvoie False


    ## ==== Tests garages ====
    print("Création de deux listes de voitures")
    list1=[car1, car2, car3, car4]
    list2=[car1, car2, car3, car3, car4]
    
    print("Création de deux garages issus des deux listes précédentes")
    g1=Garage(list1)
    g2=Garage(list2)
    
    print("Affichage des deux garages")
    g1.affiche()
    g2.affiche()

    print("Enlever les doublons")
    g2.doublons()
    g2.affiche()

    print("Ajoute voiture")
    g2.ajoute(car4)
    g2.affiche()

    print("Comptage marques")
    g1.cptMarques()
    g2.cptMarques()

## ==== Appel de la classe principale ====
Principale()  
    
    
       




