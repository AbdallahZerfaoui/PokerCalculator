from tkinter import *

valeurs={    'A' : 14,
             'K' : 13,
             'Q' : 12,
             'J' : 11,
             'T' : 10,
             '9' : 9,
             '8' : 8,
             '7' : 7,
             '6' : 6,
             '5' : 5,
             '4' : 4,
             '3' : 3,
             '2' : 2,
}

couleurs={   'h' : 4,
             'd' : 3,
             's' : 2,
             'c' : 1,
}

def graphique(h1,h2,bord,Liste,potodds='3 to 1'):
    #sys.path.append("C:\\Users\\SIMINOV\\Desktop\\Jupyter projects\\Poker\\Cards")
    fenetre = Tk()#Toplevel()   #ON OUVRE LA FENETRE TKINTER
    fenetre.title("Poker Calculator")
    #----#----#----#----#----#----#        les messages fixes           #----#----#----#----#----#----#----#
    #msg1= Label(fenetre, text ="Poker Calculator", font = "arial 12 bold", fg = "blue").grid(row = 0, columnspan = 2)

    card1_1 = PhotoImage(file ='../Cards/card_'+h1[0]+'.gif')
    card1_2 = PhotoImage(file ='../Cards/card_'+h1[1]+'.gif')
    card2_1 = PhotoImage(file ='../Cards/card_'+h2[0]+'.gif')
    card2_2 = PhotoImage(file ='../Cards/card_'+h2[1]+'.gif')
    
    
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


def graphique1(h1,h2,bord,Liste,potodds='3 to 1'):
    fenetre = Tk ()   #ON OUVRE LA FENETRE TKINTER

    #----#----#----#----#----#----#        les messages fixes           #----#----#----#----#----#----#----#
    msg1= Label(fenetre, text ="Poker Calculator", font = "arial 12 bold", fg = "blue").grid(row = 0, columnspan = 2)
    '''
    msg_vide = Label(fenetre).grid(row = 1, column = 0)
    msg_vide2 = Label(fenetre).grid(row = 5, column = 0)
 
    #----#----#----#----#----#----#        les VALID (boutons cliquables)           #----#----#----#----#----#----#
    bouton_yes = Button(fenetre, text =" <<OUI>> ", fg="green").grid(row=4, column=0)
    bouton_no = Button(fenetre, text="<<NON>>", fg = "red").grid(row=4, column=1)
    #----#----#----#----#----#----#        l'image...          #----#----#----#----#----#----#
    '''
    card1_1 = PhotoImage(file ='card_'+h1[0]+'.gif')
    card1_2 = PhotoImage(file ='card_'+h1[1]+'.gif')
    card2_1 = PhotoImage(file ='card_'+h2[0]+'.gif')
    card2_2 = PhotoImage(file ='card_'+h2[1]+'.gif')
    
    
    espace_image1 = Canvas(fenetre, width =100, height =70, bg ='white')
    espace_image1.grid(row=1 ,columnspan=12, column=3, padx =10, pady =10)
    espace_image2 = Canvas(fenetre, width =100, height =70, bg ='white')
    espace_image2.grid(row=3 ,columnspan=12, column=3, padx =10, pady =10)

    espace_image_bord = Canvas(fenetre, width =290, height =70, bg ='dark green')
    espace_image_bord.grid(row=2 ,columnspan=12, column=3, padx =100, pady =10)
    

    espace_pourcent = Canvas(fenetre, width =0, height =0, bg ='gray')
    espace_pourcent.grid(row=1 ,columnspan=1, column=3, padx =10, pady =10)
    """
    espace_potodds = Canvas(fenetre, width =70, height =70, bg ='gray')
    espace_potodds.grid(row=2 ,columnspan=1, column=3, padx =10, pady =10)
    """
    
    espace_image1.create_image(75, 35, image =card1_1)
    espace_image1.create_image(25, 35, image =card1_2)

    espace_image2.create_image(75, 35, image =card2_1)
    espace_image2.create_image(25, 35, image =card2_2)
    mot={0:"Win :",1:"Split  :",2:"Lost:"}
    for elm in Liste:
        i=Liste.index(elm)
        Label(espace_pourcent, text =mot[i]+5*" "+str(Liste[i])+'%', font = "arial 12 bold", fg = "blue").grid(row = i+1, columnspan = 1)
    
    Img=[]

    for i in range(len(bord)):
        bordi=PhotoImage(file ='card_'+bord[i]+'.gif')
        Img.append(bordi)
        
    for elm in Img:
        i=Img.index(elm)
        espace_image_bord.create_image(60*i+25, 35, image = elm)
        
 
    mainloop ()


def separateur (L,car): #permet d'obtenir juste les valeurs, ou les couleurs, des cartes de la main 
    result=[]
    for j in range(len(L)):
        if car=='h': #pour ne garder que les valeurs
            result.append(L[j][0])
        if car=='c' : #pour ne garder que les couleurs
            result.append(L[j][1])
    return result


def detect(L_poss): # fonction qui renvoie les caracteres répétés sur une nouvelle liste
    traitement=[] # initialisation
    doublon=[] # initialisation
    
    for carte in L_poss:
        if carte[0] not in traitement:
            traitement.append(carte[0]) 
        else:
            doublon.append(carte[0]) # si carte[0] est deja ds traitement alors on l'ajoute a la liste doublon
    return doublon


def convert(Liste_cartes): #converti les cartes en valeur numerique

    L_num=[]
    for i in range(len(Liste_cartes)):
        L_num.append(100*couleurs[Liste_cartes[i][1]]+valeurs[Liste_cartes[i][0]]) 
        '''
    if 14 in L_num:     #le double role de l'as
        L_num.append(1) #on ajoute la valeur 1 en plus de 14 pour l'as
        '''
    L_num.sort()#trier la liste
    return L_num


def Compare_Liste(L1,L2):
    if [L1,L2]==[[],[]]:
        return [0]# si les listes sont vides, renvoie 0
    elif L1==[]:
        return[2]# si L1 vide, renvoie 2
    elif L2==[]:
        return[1]# si L2 vide, renvoie 1
    for i in range(min(len(L1),len(L2))):
        if L1[i]>L2[i]:
            return [1]# si L1>L2 renvoie 1
        elif L1[i]<L2[i]:
            return [2]# si L2>L1 renvoie 2
    return[0]


def combinliste(seq):
    p = []
    i, imax = 0, len(seq)-1
    while i<=imax:
        s = [seq[i]]
        j, jmax = i+1, len(seq)-1
        while j<=jmax:
            a=s+[seq[j]]
            p.append(a)
            j+=1 
        i += 1 
    return p
