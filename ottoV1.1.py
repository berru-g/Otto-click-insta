#projet d automatisation de like sur insta pour projet pro

import pyautogui as pt
import pyautogui
from time import sleep
from random import randint
from colorama import Back, Fore, Style, deinit, init
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By

#Fenetre de presentation****************************************************
#racine= Tk()
Fenetre= Tk()
Fenetre.title("Otto le bot") 
Fenetre.iconbitmap(r'icon_1.ico')
photo=PhotoImage(file="presentation.png")
labl = Label(Fenetre, image=photo)
labl.pack()
#bouton_sortir = Button(Fenetre,text="Let's go",command=Fenetre.destroy)
#bouton_sortir.pack()
#OBJ: recuperer ID et MDP pour envoie *
#user_name = Label(Fenetre,text = "Username").place(x = 40, y = 300)
#user_password = Label(Fenetre,text = "Password").place(x = 40, y = 320)
#bouton_sortir = Button(Fenetre,text="Envoie",command=Fenetre.destroy)
submit_button = Button(Fenetre,text = "Démarrer",command=Fenetre.destroy).place(x = 260,y = 330)
#user_name_input_area = Entry(Fenetre,width = 30).place(x = 110,y = 300)
#user_password_entry_area = Entry(Fenetre, width = 30).place(x = 110, y = 320)
Fenetre.mainloop()

# WEB DRIVER E1 ###############################
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
sleep(1)
driver.get("https://www.instagram.com")
sleep(1)
pyautogui.typewrite("Enter")
sleep(3)
#click sur 'cookies'**************************
x, y = pyautogui.locateCenterOnScreen('cookies.png')
pyautogui.click(x, y)
sleep(1)

#connexion*partie no pris en compte*******************************************
#OBJ: recuperation de ID et MDP *
# ATTENTION BY EST OBSOLETE
#element = find_element_by_name("element_name")    REMPLACER PAR...
#element = driver.find_element(By.NAME, "element_name")
#******************************************************************************
#element = driver.find_element(By.ID,"passwd-id")
#element = driver.find_element(By.NAME, "username")
#element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.NAME, "username")
pyautogui.typewrite("username@mail.con")
pyautogui.typewrite(["enter"])
element = driver.find_element(By.NAME, "password")
pyautogui.typewrite("motdepasse")
pyautogui.typewrite(["enter"])
sleep(4)
#################################
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




