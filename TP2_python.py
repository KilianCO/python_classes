# -*- coding: utf-8 -*-
"""
06/10/22 - M2SMSD (TP 2)
Remise à niveau informatique
"""

#Exercice 1 : Méthode affichant le contenu d'une chaîne, mais consonne = étoile

def remplace(a):
    Voyelle = ["a","e","y","i","o","u"]         #On fait une liste des voyelles
    b = ""                                      #On crée un vecteur vide
    for i in range(len(a)):
        if a[i] not in Voyelle:                 #Si une lettre n'est pas dans voyelle, on la remplace par étoile
            b = b + "*"
        else:
            b = b + a[i]                        #Sinon on la laisse tel qu'elle
    return b

remplace("Bonjour")

#Exercice 2 : Palindrome --> Paramètre = Chaîne de caractères, Affiche si on a un palindrome

def palindrome(a):
    b = 0                                               #On initialise notre indicateur à 0 (= C'est un palindrome)
    for i in range(int(len(a)/2) + 1):
        if a[i] != a[len(a) - 1 - i]:                   #On va jusqu'à la moitié de la chaîne pour voir la lettre associé symétriquement
            b = 1                                       #S'il n'y a pas symétrie ce n'est pas un palindrome : b = 1
            break                                       #On peut donc sortir de la boucle
    if b == 0:
        print(a, "est un palindrome")                   #On affiche si a est un palindrome ou non
    elif b == 1:
        print(a, "n'est pas un palindrome")
        
        
palindrome("Bonjour")
palindrome("non")

#Exercice 1 : muable --> Mettre le 1er terme d'un tuple au carré, puis afficher le tuple (hors fonction)

def muable(a):
    a = (a[0]**2,a[1:len(a)])
    print(a)
    return a

a = (2,2,3)
muable(a)
print(a)

#Partie 2 : Pareil mais avec liste

def nonmuable(l):
    l[0] = l[0]*l[0]
    print(l)
    return l

l = [3,2,5]
nonmuable(l)
print(l)
    
#Exercice 2 : moyennedes éléments sauf le premier

def moyenne(l):
    m = 0
    for i in range(1,len(l)):
        m = m + l[i]
    return m/(len(l)-1)

l = [3,2,5]
moyenne(l)

Note = ['Math', 15, 16, 10, 8]
a = int(input("Insérez une note à ajouter à la fin de la liste "))
Note = Note + [a]
b = int(input("Insérez une note à ajouter au début de la liste "))

Temp = [Note[0],b]
Temp = Temp + Note[1:len(Note)]
Note = Temp

Note

print("La moyenne des notes de", Note[0], "est :", moyenne(Note))

def moyennesup(l):
    temp = []
    for i in range(len(l)):
        if l[i]>10:
            temp = temp + [l[i]]
    l = temp
    return l

moyennesup(Note[1:len(Note)-1])

#Exercice 3 : Dictionnaire Anglais (Clé) Français (Valeur)

dico = {"sun": "soleil", "beach": "plage", "corn": "maïs", "dog": "chien", "fish": "poisson"}

print(dico)

print(dico.keys()) # affiche seulement les mots anglais

print(dico.values()) # affiche seulement les traductions françaises

dico.pop("corn") # supprime l'élément dont la clé est "corn"

print(dico)



# Exercice 4


# avec les listes

def trieListe(liste):

    listeFilt = []

    listeTriee = []

    # Filtration des notes supérieures à 10

    for l in liste:

        if l[1] >= 10:

            listeFilt.append(l)

    # Tri dans l'ordre croissant des notes conservées

    for i in range(len(listeFilt)):

        indMin = 0

        for j in range(len(listeFilt)):

            if listeFilt[j][1] < listeFilt[indMin][1]:

                indMin = j

        # on met la plus petite dans la liste triée         
        listeTriee.append(listeFilt[indMin])
        
        # on l'enleve de la liste filtree
        # ainsi a la prochaine boucle on recherche la plus petite  

        listeFilt.pop(indMin)

    return listeTriee

notes = [["maths", 12], ["français", 14], ["histoire-géo", 10], ["anglais", 7], ["physique-chimie", 15]]
print(trieListe(notes)) # affiche la liste des cours avec plus de 10/20, triée dans l'ordre croissant



def fusionListes(l1, l2):

    liste = l1 + l2

    listeFilt = [liste[0]]

    for i in range(len(liste)):

        doublon = False

        for j in range(len(listeFilt)):

            if liste[i][0] == listeFilt[j][0] and liste[i][1] >= listeFilt[j][1]: # si la note est doublon et meilleure

                doublon = True

                listeFilt[j] = liste[i]

        if not doublon:

            listeFilt.append(liste[i])

    return listeFilt



notes2 = [["arts plastiques", 13], ["histoire-géo", 12], ["anglais", 9]]

print(fusionListes(notes, notes2))



# Exercice 4 (avec des dictionnaires)

def trieDico(d):

    dico = d.copy()

    dicoTrie = {}

    for i in range(len(dico)):

        x = min(dico, key = dico.get)

        if dico.get(x) >= 10:

            dicoTrie[x] = dico.get(x)

        dico.pop(x)

    return dicoTrie



notes = {"maths": 12, "français": 14, "histoire-géo": 10, "anglais": 7, "physique-chimie": 15}

print(trieDico(notes))



def fusionDico(dico1, dico2):

    d1, d2 = dico1.copy(), dico2.copy()

    for x in d2.keys():

        if not x in d1.keys() or d2[x] > d1[x]: # si pas de doublon ou si la note doublon est meilleure

            d1[x] = d2.get(x)

    return d1



notes2 = {"arts plastiques": 13, "histoire-géo": 12, "anglais": 9}

print(fusionDico(notes, notes2))


    