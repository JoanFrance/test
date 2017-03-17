from tkinter import *
import random

def impact():
    x=random.randint(0,L)
    y=random.randint(0,H)
    item=Canevas.create_image(x,y, image=balle)

def Undo():
    if len(Canevas.find_all()) > 1:
        item = Canevas.find_all()[-1]
        Canevas.delete(item)
       
def Effacer():
    
    while len(Canevas.find_all()) > 1:
        Undo()


#fenetre principale (main window)
fenetre = Tk()
fenetre.title('Cible')

#fond
photo = PhotoImage(file="tk_cible.gif")

#impact balle
balle = PhotoImage(file="cible.png")

#création du Canevas
L = 550
H = 550
Canevas = Canvas(fenetre,width = L, height =H)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
Canevas.pack()

# Bouton widget TIRER
BoutonGo = Button(fenetre, text ='Tirer', command = impact,fg='white', bg='red')
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Bouton Widget UNDO
BoutonUndo = Button(fenetre, text ='Undo', command = Undo,fg='white', bg='red')
BoutonUndo.pack(side = LEFT, padx = 10, pady = 10)

# Bouton widget EFFACER
BoutonEffacer = Button(fenetre, text ='Effacer tout', command = Effacer,fg='white', bg='red')
BoutonEffacer.pack(side = LEFT, padx = 10, pady = 10)

# Bouton widget QUITTER
BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy,fg='white', bg='black')
BoutonQuitter.pack(side = LEFT, padx = 10, pady = 10)

fenetre.mainloop()

#Source image balle: https://online-shirt-designer.ch/francais/t-shirts/une%20balle.php
