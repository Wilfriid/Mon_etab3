import time
from datetime import datetime
from menu import afficherSousMenuUtil, accueil
from models.utilisateur import Utilisateur

def ajouterUtilisateur():
    pseudo = input("Entrez le pseudo : ")
    motDePasse = input("Entrez le mot de passe : ")
    message = Utilisateur.ajouterCompte(pseudo, motDePasse)  # Enregistre le mot de passe sans hachage
    print(message)

def supprimerUtilisateur():
    pseudo = input("Entrez le pseudo de l'utilisateur à supprimer : ")
    if not Utilisateur.supprimerCompte(pseudo):
        print(f"L'utilisateur {pseudo} n'existe pas.")

def modifierUtilisateur():
    pseudo = input("Entrez le pseudo de l'utilisateur dont vous voulez modifier le mot de passe : ")
    utilisateur = Utilisateur.recuperer_utilisateur(pseudo)
    if utilisateur:
        nouveauMotDePasse = input("Entrez le nouveau mot de passe : ")
        utilisateur.modifierMotDePasse(nouveauMotDePasse)
    else:
        print(f"L'utilisateur {pseudo} n'existe pas.")

def listerUtilisateurs():
    Utilisateur.listerUtilisateurs()

def gestionUtilisateurs():
    accueil("GESTION DES UTILISATEURS")
    while True:
        afficherSousMenuUtil()
        try:
            choix = int(input("Choisissez une option dans le menu : "))
        except ValueError:
            print('Vous devez entrer un chiffre du menu !!')
            time.sleep(0.5)
            continue

        match choix:
            case 1:
                ajouterUtilisateur()
            case 2:
                supprimerUtilisateur()
            case 3:
                modifierUtilisateur()
            case 4:
                listerUtilisateurs()               
            case 5:
                break             
            case 0:
                return                   
            case _:
                print("Option invalide, veuillez réessayer !!")
                time.sleep(0.5)
                continue

