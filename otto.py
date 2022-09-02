#projet d automatisation de like sur insta pour projet pro
#    prochaine etape:
#1 - choisir le hastag à cibler
#2 - calculer le nombre de click ou scroll
import pyautogui as pt
import pyautogui
from time import sleep
from random import randint
from colorama import Back, Fore, Style, deinit, init
from tkinter import *
from tkinter import RIGHT

#racine= Tk()
Fenetre= Tk()

Fenetre.title("Otto le bot") # Donne un titre à la fenêtre (par défaut c'est Tk)
Fenetre.iconbitmap(r'icon_1.ico')
photo=PhotoImage(file="presentation.png")
labl = Label(Fenetre, image=photo)
labl.pack()
#zone_dessin = Canvas(Fenetre, width=500, height=500) #Définit les dimensions du canevas
#zone_dessin.pack() #Affiche le canevas
#zone_dessin.create_line(0,0,500,500) #Dessine une ligne en diagonale
#zone_dessin.create_rectangle(100,100,200,200) #dessine un rectangle
bouton_sortir = Button(Fenetre,text="Let's go",command=Fenetre.destroy)
bouton_sortir.pack()

Fenetre.mainloop()

int()
jeu = ["0", "1"]
ordinateur = jeu[randint(0,1)]
Pointsjoueur = 1
Pointsordinateur = 0


class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
#            pt.Click()
            print("1")
            pyautogui.click()
            Pointsjoueur = Pointsjoueur + 1
            sleep(1)

        except:
            print("0")
            pyautogui.scroll(-1200)
#            pyautogui.press(RIGHT)
            sleep(1)
            return 0


if __name__ == '__main__':
    clicker = Clicker('likeinstaWHITE.png', speed=.001)
    sleep(1)
    #Pointsjoueur = Pointsjoueur + 1
    end = 0

    while True:
        if clicker.nav_to_image() == 0:
            end += 1
            Pointsordinateur = Pointsordinateur + 1

        # End the loop
        if end > 4:
            break
        

#pyautogui.alert('Otto a terminé !', Pointsjoueur)
print(Fore.GREEN + Style.NORMAL + 'Resultat:')
print("Click: ", Pointsjoueur)
print("Scroll: ", Pointsordinateur)
print(Style.RESET_ALL + 'for Run: write py like-insta.py')
        
session= Tk()
session.title("Otto le bot")
session.iconbitmap(r'icon_1.ico')
photo=PhotoImage(file="fin.png")
labl = Label(session, image=photo)
labl.pack()
bouton_sortir = Button(session,text="Good day",command=session.destroy)
bouton_sortir.pack()

session.mainloop()




