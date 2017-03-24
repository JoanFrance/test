from numpy import*
from tkinter import*





####creation de la matrice
def init(n,p):
    return(zeros([n,p]))

M=init(6,7)
#print(M)


x0=x1=x2=x3=x4=x5=x6=5

#Initialisations des coordonées pour le plaçage des jetons 
L0=72    
L1=215
L2=358
L3=501
L4=644
L5=786
L6=930

H0=687
H1=687
H2=687
H3=687
H4=687
H5=687
H6=687

#initialisation du compteur du joueur
c=0
n=1

def rajout0():
    global x0,M,n,H0,L0,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L0,H0,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L0,H0,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1
    M[x0,0]=n
    x0=x0-1
    print(M)
    c=c+1
    H0=H0-124.5 #Permet de placer les jetons les uns au dessus des autres

def rajout1():
    global x1,M,n,H1,L1,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    if c%2==0:
         Canevas.create_image(L1,H1,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L1,H1,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1
    M[x1,1]=n
    x1=x1-1
    print(M)
    c=c+1
    H1=H1-124.5 #Permet de placer les jetons les uns au dessus des autres

def rajout2():
    global x2,M,n,H2,L2,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L2,H2,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L2,H2,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1

    M[x2,2]=n
    x2=x2-1
    print(M)
    c=c+1
    H2=H2-124.5 #Permet de placer les jetons les uns au dessus des autres
    
def rajout3():
    global x3,M,n,H3,L3,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L3,H3,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L3,H3,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1

    M[x3,3]=n
    x3=x3-1
    print(M)
    c=c+1
    H3=H3-124.5 #Permet de placer les jetons les uns au dessus des autres

    
def rajout4():
    global x4,M,n,H4,L4,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L4,H4,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L4,H4,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1

    M[x4,4]=n
    x4=x4-1
    print(M)
    c=c+1
    H4=H4-124.5 #Permet de placer les jetons les uns au dessus des autres

def rajout5():
    global x5,M,n,H5,L5,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L5,H5,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L5,H5,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1

    M[x5,5]=n
    x5=x5-1
    print(M)
    c=c+1
    H5=H5-124.5 #Permet de placer les jetons les uns au dessus des autres

def rajout6():
    global x6,M,n,H6,L6,c
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    
    if c%2==0:
         Canevas.create_image(L6,H6,image=jetonj) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=2
    else:
         Canevas.create_image(L6,H6,image=jetonr) #Permet de placer l'image du jeton aux coordonnées données ci-dessus
         n=1

    M[x6,6]=n
    x6=x6-1
    print(M)
    c=c+1
    H6=H6-124.5 #Permet de placer les jetons les uns au dessus des autres


###creation de la fentre principale


Mafenetre=Tk()
Mafenetre.title('puissance 4')

photo=PhotoImage(file="grille.GIF")
jetonj = PhotoImage(file="jetonjaune.GIF")
jetonr = PhotoImage(file="jetonrouge.GIF")
Largeur = 1500
Hauteur = 750

photo=PhotoImage(file="grille.GIF")
Largeur = 1500
Hauteur = 750

Canevas = Canvas(Mafenetre, width = Largeur, height= Hauteur)
item=Canevas.create_image(0,0,anchor=NW, image=photo)
Canevas.pack()


#creation d'un bouton pour la colonne 0
BoutonColonne0=Button(Mafenetre,text='Placer1',command=rajout0)
BoutonColonne0.pack(side=LEFT,padx=50,pady=5)


#creation d'un bouton pour la colonne 1
BoutonColonne1=Button(Mafenetre,text='Placer2',command=rajout1)
BoutonColonne1.pack(side=LEFT,padx=45,pady=5)


#creation d'un bouton pour la colonne 2
BoutonColonne2=Button(Mafenetre,text='Placer3',command=rajout2)
BoutonColonne2.pack(side=LEFT,padx=43,pady=5)


#creation d'un bouton pour la colonne 3
BoutonColonne3=Button(Mafenetre,text='Placer4',command=rajout3)
BoutonColonne3.pack(side=LEFT,padx=55,pady=5)


#creation d'un bouton pour la colonne 4
BoutonColonne4=Button(Mafenetre,text='Placer5',command=rajout4)
BoutonColonne4.pack(side=LEFT,padx=40,pady=5)


#creation d'un bouton pour la colonne 5
BoutonColonne5=Button(Mafenetre,text='Placer6',command=rajout5)
BoutonColonne5.pack(side=LEFT,padx=50,pady=5)


#creation d'un bouton pour la colonne 6
BoutonColonne6=Button(Mafenetre,text='Placer7',command=rajout6)
BoutonColonne6.pack(side=LEFT,padx=50,pady=5)



#creation d'un bouton Reset
#BoutonReset=Button(Mafenetre,text='Recommencer',command=rajout)
#BoutonReset.pack(side=TOP,padx=5,pady=5)


Mafenetre.mainloop()

print(M)
###fin creation matrice

#Fonction recherche victoire


#Partie recherche par balayage de matrice
##Valeur jeton vide  =0
##Valeur jeton rouge =2
##Valeur jeton jaune =1

def Victoire():

    def horizontal():
        for x in range(3):
            for y in range(5):
                if M[x,y]==1 and M[x,y+1]==1 and M[x,y+2]==1 and M[x,y+3]==1 :
                    return("rouge a gagné") ##Completer par une animation ? + son ?
                if M[x,y]==2 and M[x,y+1]==2 and M[x,y+2]==2 and M[x,y+3]==2 :
                    return("jaune a gagné")
            
    def vertical():
        for x in range(6):
            for y in range(2):
                if M[x,y]==1 and M[x,y+1]==1 and M(x,y+2)==1 and M(x,y+3)==1 :
                    return("rouge a gagné")
                if M[x,y]==2 and M[x,y+1]==2 and M(x,y+2)==2 and M(x,y+3)==2 :
                    return("jaune a gagné")

    def diagonale_bas_droite():
        for x in range(3):
            for y in range(2):
                if M[x,y]==1 and M(x+1,y+1)==1 and M(x+2,y+2)==1 and M(x+3,y+3)==1 :
                   return("rouge a gagné")
                if M[x,y]==2 and M(x+1,y+1)==2 and M(x+2,y+2)==2 and M(x+3,y+3)==2 :
                   return("jaune a gagné")
            
    def diagonale_bas_gauche():
        for x in range(3) :
            for y in range(2):
                if M(x+3,y)==1 and M(x+2,y+1)==1 and M(x+1,y+2)==1 and M(x,y+3)==1 :
                    return("rouge a gagné)












