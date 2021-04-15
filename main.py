# *-* coding: utf-8 -*-

import math
import random
import time
#from tkinter import *
#from tkinter.ttk import *
from hands_value import *
from basic_functions import *

options={   0 : hauteur,
            1 : paire,
            2 : double_paire,
            3 : brelan,
            4 : quinte,
            5 : flush,
            6 : full_house,
            7 : carre,
            8 : quinte_flush,
        }

def compare(main1,main2,bord):
    
    possibilite1=convert(main1+bord) # façon de detecter paire, double, brelan, full et carre
    possibilite2=convert(main2+bord)
    
    L=list(range(8)) # 8 is the code of the highest hand in poker "quinte flush" 
    L.sort(reverse=True)
    for i in L:
        '''
        if (options[i](possibilite1), options[i](possibilite2))!=([],[]):
        '''
        x=Compare_Liste(options[i](possibilite1), options[i](possibilite2))
                #print (options[0](possibilite_num))
        if x==[0] and options[i](possibilite1)!=[]: # pour le cas on a quelque chose et pourtant split
            return [0]
        
        if x!=[0]:
            return x
    return [0]

def graphique(h1,h2,bord,Liste,potodds='3 to 1'):
    #sys.path.append("C:\\Users\\SIMINOV\\Desktop\\Jupyter projects\\Poker\\Cards")
    fenetre = Tk()#Toplevel()   #ON OUVRE LA FENETRE TKINTER
    fenetre.title("Poker Calculator")
    #----#----#----#----#----#----#        les messages fixes           #----#----#----#----#----#----#----#
    #msg1= Label(fenetre, text ="Poker Calculator", font = "arial 12 bold", fg = "blue").grid(row = 0, columnspan = 2)

    card1_1 = PhotoImage(file ='.\Cards/card_'+h1[0]+'.gif')
    card1_2 = PhotoImage(file ='.\Cards/card_'+h1[1]+'.gif')
    card2_1 = PhotoImage(file ='.\Cards/card_'+h2[0]+'.gif')
    card2_2 = PhotoImage(file ='.\Cards/card_'+h2[1]+'.gif')
    
    
    espace_image1 = Canvas(fenetre, width =100, height =70, bg ='white')
    espace_image1.grid(row=1 ,columnspan=12, column=3, padx =10, pady =10)
    espace_image2 = Canvas(fenetre, width =100, height =70, bg ='white')
    espace_image2.grid(row=3 ,columnspan=12, column=3, padx =10, pady =10)

    espace_image_bord = Canvas(fenetre, width =290, height =70, bg ='dark green')
    espace_image_bord.grid(row=2 ,columnspan=12, column=3, padx =100, pady =10)
    

    espace_pourcent = Canvas(fenetre, width =0, height =0, bg ='gray')
    espace_pourcent.grid(row=1 ,columnspan=1, column=3, padx =10, pady =10)
    
    espace_image1.create_image(75, 35, image =card1_1)
    espace_image1.create_image(25, 35, image =card1_2)

    espace_image2.create_image(75, 35, image =card2_1)
    espace_image2.create_image(25, 35, image =card2_2)
    mot={0:"Player 1 :",1:"Split  :",2:"Player 2 :"}
    for elm in Liste:
        i=Liste.index(elm)
        Label(espace_pourcent, text =
              mot[i]+5*" "+str(Liste[i])+'%', font = "arial 12 bold", fg = "blue").grid(row = i+3, columnspan = 1)
    
    Img=[]

    for i in range(len(bord)):
        bordi=PhotoImage(file ='Cards/card_'+bord[i]+'.gif')
        Img.append(bordi)
        
    for elm in Img:
        i=Img.index(elm)
        espace_image_bord.create_image(60*i+25, 35, image = elm)
    """   
    #Buttons
    photo = PhotoImage(file = 'Cards/card_Ah.gif')
    Button(fenetre, text = 'Click Me !', image = photo).pack(side = TOP)
    """
    mainloop ()
    

def main_preflop(main1,main2):
    t1=time.time()
    hauteur='23456789TJQKA'
    couleur='hdsc'
    jeu=[] # initialisation
    nbr_simu=5000 # nombre de test pour le montecarlo
    players=[0.0,0.0,0.0]
    for c in couleur:
        jeu+=[h+c for h in hauteur]
    
    jeu=[x for x in jeu if x not in main1+main2]#moins(jeu,main1+main2)
    '''
    possibilite1=convert(main1+bord) 
    possibilite2=convert(main2+bord)
    '''
    for i in range(nbr_simu):
        
        #print len(jeu)
    
        carte_commune=random.sample(jeu,5) # genere plusieurs flop
        #print carte_commune
        test=compare(main1,main2,carte_commune)
        players[(1-test[0])%3]+=1 # fonction bizare pour mettre le split au milieu
    
    t2=time.time()
    print ([100*players[0]/nbr_simu,100*players[1]/nbr_simu,100*players[2]/nbr_simu])
    print(t2-t1, " s")
    
    #end = timeit.timeit()
    #print(1000*(end-start), " ms")
    Res = [int(1E4*players[0]/nbr_simu)/100.0,int(1E4*players[1]/nbr_simu)/100.0,int(1E4*players[2]/nbr_simu)/100.0]
    graphique(main1,main2,[],Res)

    
def main_flop(main1,main2,flop):
    t1=time.time()
    hauteur='23456789TJQKA'
    couleur='hdsc'
    jeu=[] # initialisation
    
    players=[0.0,0.0,0.0]
    for c in couleur:
        jeu+=[h+c for h in hauteur]
    
    jeu=[x for x in jeu if x not in main1+main2+flop]#moins(jeu,main1+main2+flop)
    
    paire=combinliste(jeu)
    nbr_simu=len(paire)
    for carte_commune in paire:
        
        test=compare(main1,main2,flop+carte_commune)
        players[(1-test[0])%3]+=1 # fonction bizare pour mettre le split au milieu
   
    t2=time.time()
    print ([100*players[0]/nbr_simu,100*players[1]/nbr_simu,100*players[2]/nbr_simu])
    print(t2-t1, " s")
    Res = [int(1E4*players[0]/nbr_simu)/100.0,int(1E4*players[1]/nbr_simu)/100.0,int(1E4*players[2]/nbr_simu)/100.0]
    graphique(main1,main2,flop,Res)

#il y a un probleme on a pas besoin de faire 10000 simulation on a juste 48 cartes
def main_turn(main1,main2,flop):
    t1=time.time()
    hauteur='23456789TJQKA'
    couleur='hdsc'
    jeu=[] # initialisation
    nbr_simu=10000
    
    players=[0.0,0.0,0.0]
    for c in couleur:
        jeu+=[h+c for h in hauteur]

    jeu=[x for x in jeu if x not in main1+main2+flop]#moins(jeu,main1+main2+flop)
    
    for i in range(nbr_simu):
        hauteur=random.sample(jeu,1)

        
        test=compare(main1,main2,hauteur+flop)
        players[(1-test[0])%3]+=1 # fonction bizare pour mettre le split au milieu
   
    t2=time.time()
    print(t2-t1, " s")
    Res = [int(1E4*players[0]/nbr_simu)/100.0,int(1E4*players[1]/nbr_simu)/100.0,int(1E4*players[2]/nbr_simu)/100.0]
    graphique(main1,main2,flop,Res)

    
def main_calculator(main1=[],main2=[],bord=[], step=""):
    if (step=="preflop"):
        main_preflop(main1,main2)
    elif(step=="flop"):
        main_flop(main1,main2,bord)
    elif(step==""):
        True
    else:
        main_turn(main1,main2,bord)


#TEST

main1  =['Ah','Kh']
main2  =['9h','Ks']
#h1=['Ah','Kd']
#h2=['Qh','As']
bord   =['8c','Ks','Kc','Qc','9h']
bord1  =['8c','Qs','Kc','Ac','9h']
bord_f =['8h','Qh','Kc','Ac','9h']
bord_qf=['Th','Qh','Kc','Ac','Jh']
flop   =['As','Ac','3s']
turn   =['As','Ac','3s','2h']

#calculation
main_calculator(main1,main2,step="preflop")
        
