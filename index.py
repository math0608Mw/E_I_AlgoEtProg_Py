##Intro
from random import randint


print( "Bienvenue au juste nombre !")
print( "----- MENU -----")
print( "[1] Jouer")
print( "[2] Scores")
print( "[3] Quitter")

cpt = 0

## Menu
c_menu = int(input("Choisissez une option :"))


## Mode Jouer
if c_menu == 1 :
  prenom = input("Bonjour cher.ère aventurier.ère !\n Comment tu surnommes tu ?")
  print("Bienvenue", prenom, "!") 
  print("Je m'appelle MathMw et je suis le maître du jeu du 'juste nombre'.\nLe but est de trouver le nombre que je vais générer aléatoirement.\nje te propose 3 modes de jeu :\n- Niveau 1 : De 1 à 10.\n- Niveau 2 : De 1 à 100.\n- Niveau 3 : De 1 à 1000.")
  print("Le but est de trouver le nombre que je vais générer aléatoirement.")
  c_level = int(input("Quel niveau veux-tu choisir ?"))

  if c_level == 1 :
      print("D'accord, allons-y !")
      rdm_nbre = randint(1,10)

      while True:
         nbre = int(input("Quel est ton nombre ?"))
         cpt = cpt + 1
         if nbre > rdm_nbre :
             print("c'est moins !")
         elif nbre < rdm_nbre :
             print("c'est plus !")
         elif nbre == rdm_nbre :
            print("Bravo ! Tu as trouvé en ",cpt," coups !")
            break
         if cpt == 5 :
            print("Dommage, tu as utilisé tes 5 coups, tu as perdu !")


if c_level == 2 :
      print("D'accord, allons-y !")
      rdm_nbre = randint(1,100)

      while True:
         nbre = int(input("Quel est ton nombre ?"))
         cpt = cpt + 1
         if nbre > rdm_nbre :
             print("c'est moins !")
         elif nbre < rdm_nbre :
             print("c'est plus !")
         elif nbre == rdm_nbre :
            print("Bravo ! Tu as trouvé en ",cpt," coups !")
            break
         if cpt == 5 :
            print("Dommage, tu as utilisé tes 5 coups, tu as perdu !")


if c_level == 3 :
      print("D'accord, allons-y !")
      rdm_nbre = randint(1,1000)

      while True:
         nbre = int(input("Quel est ton nombre ?"))
         cpt = cpt + 1
         if nbre > rdm_nbre :
             print("c'est moins !")
         elif nbre < rdm_nbre :
             print("c'est plus !")
         elif nbre == rdm_nbre :
            print("Bravo ! Tu as trouvé en ",cpt," coups !")
            break
         if cpt == 5 :
            print("Dommage, tu as utilisé tes 5 coups, tu as perdu !") 
            break 


## Scores

if c_menu == 2 :
    fichier = open("scores.txt", "r")
    print(fichier.read())
    fichier.close()

## Quitter

if c_menu == 3 :
    quit()


