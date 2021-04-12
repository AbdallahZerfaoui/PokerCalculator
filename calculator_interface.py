from tkinter import *
#import numpy as np



def clicked(card_high,color):
    #inputs
    width=900
    height =610
    width_cards=int(50/1.5)
    height_cards =int(70/1.5)
    #lbl.configure(text="Button was clicked !!")
    img_p1=PhotoImage(file=".\\Cards\\card_As.gif")
    #espace_image_p1 = Canvas(window, width =100, height =35, bg ='grey')
    #espace_image_p1.place(x=3*width_cards+350, y=-150+int(height_cards*(14-valeurs[card_high])/2))
    #espace_image_p1.create_image(255, 125, image =img_p1)
    #res = "Welcome to " + txt.get()
    #lbl.configure(text= res)
    #create a button
    """
    btn = Button(window, bg="grey", fg="red", image=Images[14-valeurs[card_high]][couleurs[color]-1],
                       height=height_cards,width=width_cards)
    """
    #btn.place(c=500, y=500)#button
    #btn.place(x=3*width_cards+350, y=-150+int(height_cards*(14-valeurs[card_high])/2))#button
    btn_p1 = Button(window, bg="grey", fg="red", image=img_p1,
                   height=height_cards+15,width=width_cards+7)

valeurs={'A' : 14,
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
#inputs
width=900
height =610
width_cards=int(50/1.5)
height_cards =int(70/1.5)
#create a window    
window = Tk()
window.title("Poker Calculator")
#create a label
#lbl = Label(window, text="Hello", font=("Arial Bold", 25))
#lbl.grid(column=0, row=0)
#size of the window
window.geometry(str(width)+"x"+str(height))
#create an image space
"""
img=PhotoImage(file=".\\Cards\\card_As.gif")
espace_image = Canvas(window, width =200, height =910, bg ='blue')
espace_image.grid(row=0 ,columnspan=12, column=0, padx =10, pady =10)
espace_image.create_image(25, 35, image =img)
"""
"""
btn = Button(window, text="Click Me", bg="orange", fg="red",
             image="card_As.gif",command=clicked)
"""
#add the poker table
img=PhotoImage(file=".\\Cards\\table_poker4.gif")
espace_image = Canvas(window, width =510, height =245, bg ='blue')
espace_image.place(x=3*width_cards+150, y=-125+int(height_cards*13/2))
espace_image.create_image(255, 125, image =img)

#add players cards
img_p1=PhotoImage(file=".\\Cards\\card_Ah.gif")
btn_p1 = Button(window, bg="grey", fg="red", image=img_p1,
                   height=height_cards+15,width=width_cards+7)
btn_p1.place(x=3*width_cards+350, y=-150+int(height_cards*13/2))#button

#Main
deck=[]
L=[]
Images=[]
for i in range(13):
    L.append(list(range(4)))
    Images.append(list(range(4)))


for card_high in valeurs:#{"A":14, "K":13}:
    highs=[]
    for color in couleurs:
        Images[14-valeurs[card_high]][couleurs[color]-1]=\
                                    PhotoImage(file=".\\Cards\\card_"+card_high+color+".gif",
                                               height=height_cards,width=width_cards)
        #create a button
        L[14-valeurs[card_high]][couleurs[color]-1] = \
                    Button(window, bg="grey", fg="red", image=Images[14-valeurs[card_high]][couleurs[color]-1],
                           height=height_cards,width=width_cards, command=clicked(card_high,color))
        
        L[14-valeurs[card_high]][couleurs[color]-1].\
                                        place(x=width_cards*(couleurs[color]-1), y=height_cards*(14-valeurs[card_high]))#button
                                        #grid(column=couleurs[color]-1, row=14-valeurs[card_high])#button
        
        highs.append(L[14-valeurs[card_high]][couleurs[color]-1])
    deck.append(highs)

"""
table = PhotoImage(file=".\\Cards\\card_"+card_high+color+".gif",
                                               height=height_cards,width=width_cards)
table.grid(column=5, row=5)
"""

"""
img_p1=PhotoImage(file=".\\Cards\\card_Ah.gif")
espace_image_p1 = Canvas(window, width =100, height =35, bg ='grey')
espace_image_p1.place(x=3*width_cards+350, y=-150+int(height_cards*(14-valeurs[card_high])/2))
espace_image_p1.create_image(255, 125, image =img_p1)

img_p2=PhotoImage(file=".\\Cards\\card_Ks.gif")
espace_image_p2 = Canvas(window, width =100, height =35, bg ='grey')
espace_image_p2.place(x=3*width_cards+350, y=105+int(height_cards*(14-valeurs[card_high])/2))
espace_image_p2.create_image(255, 125, image =img_p2)
"""

#espace_image1 = Canvas(window, width =100, height =70, bg ='blue')
#espace_image1.grid(row=5, ,columnspan=12, column=5, padx =10, pady =10)
#create an input box
#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)
#txt.focus()

#window.mainloop()
