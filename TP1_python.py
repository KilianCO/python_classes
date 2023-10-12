# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:58:49 2022

@author: Kilian COLLET
"""


# Exercice 1
nom = input("Entrer votre nom :")
print("bonjour",nom)



# Exercice 2
a = int(input("Entrer la variable a :"))
b = int(input("Entrer la variable b :"))
ope = input("Entrer l'opération :")

if(ope == '+') :
    res=a+b
elif (ope == '-') :
    res=a-b
elif (ope == '*') :
    res=a*b
elif (ope == '/') :
    res=a/b
else :
    print('error')

print(res)



# Exercice 3
import random

res = random.random()
print(res)
if res <= 0.5:
    piece = 'pile'
else :
    piece = 'face'
print(piece)
choix=input("Ecrire 'pile' ou 'face' : ")
if (piece==choix):
    print('Gagné !')
else:
    print('Perdu !')
print('Vous avez prédit',choix,'et il y a eu',piece)


# Exercice 4
i=0
traj=[i]
while (i<=4):
    r=random.random()
    if r<=0.5:
        i=i+1
        traj=traj+[i]
    else:
        i=i-1
        traj=traj+[i]
print(i,traj)



# Exercice 5
a=float(input('Entrer un décimal :'))
a_bis=int(a)
if (a-a_bis) >= 0.5 :
    a=a_bis+1
else:
    a=a_bis
print(a)


# Exercice 6
x=[0,2,4,5,7]
y=[1,2.5,3,7.02,8]

i=0
j=0
z=[]

# Tant qu'on est pas sortis, on remplit avec le min
while (i<len(x)) & (j<len(y)) :
    if x[i]<=y[j]:
        z=z+[x[i]]
        i=i+1
    else:
        z=z+[y[j]]
        j=j+1
        
# Une fois que i (ou j) est arrivé au bout, on remplit avec le reste de l'autre
if i==len(x):
    z=z+y[j:len(y)]
else:
    z=z+x[i:len(x)]
    
print(z)



# Exercice 7
import random
n = 10
x=[]

for 




