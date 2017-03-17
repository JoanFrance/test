from numpy import*
from tkinter import*
def init(n,p):
    return(zeros([n,p]))

M=init(6,7)
#print(M)
n=1

x0=x1=x2=x3=x4=x5=x6=5


def rajout0():
    global x0,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x0,0]=n
    x0=x0-1
    print(M)
    
def rajout1():
    global x1,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x1,1]=n
    x1=x1-1
    print(M)

def rajout2():
    global x2,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x2,2]=n
    x2=x2-1
    print(M)

def rajout3():
    global x3,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x3,3]=n
    x3=x3-1
    print(M)
    
def rajout4():
    global x4,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x4,4]=n
    x4=x4-1
    print(M)

def rajout5():
    global x5,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x5,5]=n
    x5=x5-1
    print(M)

def rajout6():
    global x6,M,n
    #je recup les coordonnes en fonction de y et x je place n dans la colonne y pour le joueur n)
    M[x6,6]=n
    x6=x6-1
    print(M)    



###creation de la fentre principale


Mafenetre=Tk()
Mafenetre.title('puissance 4')

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
