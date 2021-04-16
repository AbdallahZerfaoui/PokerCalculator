# *-* coding: utf-8 -*-

import math
import random
import time
from tkinter import*
#import dicos


#===============================================================================
def hauteur(Liste_carte): # détermine la hauteur d'une main
    
    A='1'+14*'0' # initialisation
    B=[] # initialisation
    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A

    A=A[::-1] # inverse A
    n=0
    for i in range(len(A)): # on parcourt la liste
        if A[i]=='1' and n<5:
            B.append(14-i) # renvoie la valeur de la hauteur
            n+=1

    return B
# ======================================================================================================
    
def paire(Liste_carte): # determine si le joueur a une paire
    A='1'+14*'0' # initialisation

    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A

    B=[] # initialisation
    if A.count('2')!=0: # si il n'y a q'un doublon
        A=A[::-1] # inverse A
        B.append(14-A.index('2'))
        n=0
        for i in range(len(A)): # on parcourt la liste
            if A[i]=='1' and n<3:
                B.append(14-i)
                n+=1
               
        return B
    else:
        return []

# ========================================================================================================
    
def double_paire(Liste_carte): # determine si le joueur a une double paire
    A='1'+14*'0' # initialisation
    '''
    Liste_hauteur=separateur(Liste_carte,'h') # pour traiter que les valeurs de Liste_carte et non les couleurs
    Liste_doublon=detect(Liste_hauteur)  # renvoie juste les caracteres répétés de Liste_hauteur
    '''
    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A

    if A.count('2')>=2: 
        A=A[::-1] # inverse A
        B=A[A.index('2')+1::]
        C=[14-A.index('2'),14-B.index('2')-1]
        for i in range(len(A)):
            if A[i]!='2' and A[i]!='0':
                C.append(14-i)
                return C # affiche [c1,c2,c3] où c1 et c2 sont les paires et c3 la hauteur du reste de la main
        
                                
    else:
        return []

# ================================================================================
        
def brelan(Liste_carte): # determine si le joueur a un brelan
 
    A='1'+14*'0' # initialisation

    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A

    B=[] # initialisation
    if A.count('3')!=0: # si il n'y a q'un doublon
        A=A[::-1] # inverse A
        B.append(14-A.index('3'))
        n=0
        for i in range(len(A)):
            if A[i]=='1' and n<2:
                B.append(14-i)
                n+=1
               
        return B
    else:
        return []
# ===============================================================================
   
def quinte(Liste_carte): # determine si le joueur a une suite
    A='11'+13*'0' # initialisation
    hauteur=0 # initialisation
    for i in Liste_carte:   #placer les cartes
        if A[i%100]=='0':
            A=str(int(A)+10**(14-(i%100))) # remplissage de A
    A=A[1::]#pour connecter l'As et le 2
    A=A+'0'#rajouter un zero pour la condition d'arret
    #print A
    A=str(int(A))#enlever les premiers zeros
    
    for i in range(A.count('1')):
        j=A.index('1')
        hauteur=hauteur+j+1
        #print A, j, A[j:j+5:]
        if j+5<len(A):
            if A[j:j+5:]=='11111':
                return [hauteur+4]#a cause du 1 artificiel du début
        A=A[j+1::]
        
    return []

# =================================================================================
           
def flush(Liste_carte): # determine si le joueur a un flush
    result=[] # initialisation
    C='1'+5*'0' # initialisation
    for i in Liste_carte:
        C=str(int(C)+10**(5-(i//100))) # remplissage C
        if C.count('5')>=1:
            couleur=C.index('5')
            for elem in Liste_carte:
                if elem//100==couleur:
                    result.append(elem)
            return result # affiche l'ensemble des carte de la même couleur
    return []

# =================================================================================
                 
def full_house(Liste_carte): # determine si le joueur a un full
    A='1'+14*'0' # initialisation
    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A
   
    if A.count('3')==1 and A.count('2')==1: # si il n'y a q'un doubl
        A=A[::-1]
        return [14-A.index('3'),14-A.index('2')] # affiche [c1,c2] où c1 est le triplet et c2 la paire

    return []

# ================================================================================

def carre(Liste_carte): # determine si le joueur a un carre
    
    A='1'+14*'0' # initialisation
    for i in Liste_carte:
        A=str(int(A)+10**(14-(i%100))) # remplissage de A
    B=[] # initialisation
    if A.count('4')>=1:
        A=A[::-1] # inverse A
        B.append(14-A.index('4'))
        for i in range(len(A)):
            if A[i]!='4' and A[i]!='0':
                B.append(14-i)
                return B # affiche [c1,c2] où c1 est la carré et c2 la hauteur du reste de la main

    return []



# ==================================================================================
    
def quinte_flush(Liste_carte): # determine si le joueur a une quinte flush
    L=flush(Liste_carte)
    if L!=[]:
        if quinte(L)!=[]:
            return quinte(L) # affiche la suite au complet
        else:
            return []
