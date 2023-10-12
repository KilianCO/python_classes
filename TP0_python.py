# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:17:45 2022

@author: Kilian COLLET
"""

# Affiche
print("Hello");

# Modulo
a=7%3;
print(a);

# Affiche le type d'une variable
a=2.14*3;
print(type(a));

# Conversion de type
i=3
s=str(i)
s="4"
i=int(s)
print(type(s),type(i))

# Avec deux chaines
a="chat"
b="souris"
print(a,b) #renvoie chat souris
print(a+b) #renvoie chatsouris
print(a,b,sep=";") #chat;souris

#### Les Listes ####
# Structure de données contenant une série de valeurs
# Peuvent avoir des types différents
a=["chat","souris"] #que des str
t=[3,2.5,4] #que des int/float
m=["chat",3] #mix

# On peut appeler les éléments d'une liste par leur position
# Les indentations commencent à 0
print(a[0]) #affiche chat
print(t[1]) #affiche 2.5

# On peut faire les mêmes opérations que sur les chaines
a=["chat","souris"]
b=[3]
print(a+b)
print(2*a)



# Création d'une liste vide
l=[]
l=l+[2]
print(l)

l.append(3) #autre méthode
print(l)



# Récupérer une portion de liste
# Modèle
# liste[début:fin:pas]
x=[0,1,2,3,4]
x[0:2] #renvoie [0,1]
x[:1] #renvoie [0]
x[0:5:2] #renvoie [0,2,4]



# Fonction len()
# Renvoie la longueur de la liste
len(x)



# Fonction range()
# Modèle
# range(début,fin,pas)

# Génère des entiers dans un intervalle
list(range(10)) #génère une liste de 0 à 9
list(range(2,5)) #génère [2,3,4]
list(range(0,1000,400)) #génère [0,400,800]
list(range(4,0,-1)) #renvoie [4,3,2,1]



# On peut créer des listes de listes
a=["chat","souris"]
b=["chat","poisson"]
c=[a,b]
c #renvoie [['chat', 'souris'], ['chat', 'poisson']]
c[1] #renvoie ['chat', 'poisson']
c[1][0] #renvoie 'chat'



# Les fonctions min(), max() et sum() existent



# Boucles et comparaisons
# Boucle for
a=['chat','souris','poisson']
for animal in a:
    print(animal)
print("c'est fini")

for animal in a[1:3]:
    print(animal)

for i in range(len(a)):
    print(a[i])

# Comparaisons
# == ; =! ; > ; >= ; < ; <=
# Python renvoie TRUE ou FALSE, ce sont des booléens
2 == 3 #renvoie false

# On peut faire des comparaisons sur des chaines de caractères : ordre lexicographique

# Boucle WHILE
# Une série d'instructions executées tant que la condition est vraie
i=1
while i<=4:
    print(i)
    i+=1
# affiche 1 2 3 4

# Autre exemple avec input qui permet de demander une valeur à l'utilisateur
i=0
while i<10 :
    r=input("Rentrer un nombre supérieur à 10 :") # r est une chaine de carac str
    i=int(r) #conversion en entier int


# Branchement conditionnel
# if condition :
#    instructions
# else :
#    instructions
    
i=input("un entier")
i=int(i)
if i<10 :
    i=i*10
else :
    i=i-10
print(i)


p=float(input('prise'))
c=int(input('code'))
if(c==1) :
    p=p*2
elif (c==2) :
    p = p*3
else:
    p=p*4
print(p)






























