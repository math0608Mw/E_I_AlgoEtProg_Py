##Intro
print( "Bienvenue au juste nombre !")
print( "----- MENU -----")
print( "[1] Jouer")
print( "[2] Scores")
print( "[3] Quitter")


## Menu
c_menu = int(input("Choisissez une option :"))


## Mode Jouer
if c_menu == 1 :
  prenom = input("Bonjour cher.ère aventurier.ère !\n Comment tu surnommes tu ?")
  print("Bienvenue", prenom, "!") 
  print("Je m'appelle MathMw et je suis le maître du jeu du 'juste nombre'.\nLe but est de trouver le nombre que je vais générer aléatoirement.\nje te propose 3 modes de jeu :\n- Niveau 1 : De 1 à 10.\n- Niveau 2 : De 1 à 100.\n- Niveau 3 : De 1 à 1000.")
  print("Le but est de trouver le nombre que je vais générer aléatoirement.")
  c_mode = int(input("Quel mode veux-tu choisir ?"))

  if c_mode == 1 :
      print("mode 1 !")

if c_mode == 2 :
      print("mode 2 !")


if c_mode == 3 :
      print("mode 3 !")      


## Scores

if c_menu == 2 :
    fichier = open("data.txt", "r")
    print(fichier.read())
    fichier.close()

## Quitter

if c_menu == 3 :
    quit()


