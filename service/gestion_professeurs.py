import time
from menu import afficherSousMenuProf, accueil
from Professeur.professeur import Professeur

def ajouterProfesseur():
    dateNaissance = input("Entrez la date de naissance (YYYY-MM-DD) : ")
    ville = input("Entrez la ville : ")
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    telephone = input("Entrez le numéro de téléphone : ")
    vacant = input("Est-ce vacant ? (oui/non) : ").lower() == 'oui'
    matiereEnseigne = input("Entrez la matière enseignée : ")
    prochainCours = input("Entrez le sujet du prochain cours : ")
    sujetProchaineReunion = input("Entrez le sujet de la prochaine réunion : ")

    professeur = Professeur(dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion)
    Professeur.ajouter(professeur)
    print(f"Professeur {prenom} {nom} ajouté avec succès.")

def listerProfesseurs():
    professeurs = Professeur.obtenir_professeur()
    if professeurs:
        print("Liste des professeurs :")
        for prof in professeurs:
            print(prof)
    else:
        print("Aucun professeur enregistré.")

def modifierProfesseur():
    identifiant = int(input("Entrez l'identifiant du professeur à modifier : "))
    professeur = Professeur.obtenir(identifiant)
    if professeur:
        print(f"Modification du professeur : {professeur}")
        # Demande des nouvelles informations
        professeur.set_date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD) : ") or professeur.dateNaissance
        professeur.set_ville = input("Nouvelle ville : ") or professeur.ville
        professeur.set_prenom = input("Nouveau prénom : ") or professeur.prenom
        professeur.set_nom = input("Nouveau nom : ") or professeur.nom
        professeur.set_telephone = input("Nouveau téléphone : ") or professeur.telephone
        professeur.set_vacant = input("Est-ce vacant ? (oui/non) : ").lower() == 'oui'
        professeur.set_matiereEnseigne = input("Nouvelle matière enseignée : ") or professeur.matiereEnseigne
        professeur.set_prochainCours = input("Nouveau sujet du prochain cours : ") or professeur.prochainCours
        professeur.set_sujetProchaineReunion = input("Nouveau sujet de la prochaine réunion : ") or professeur.sujetProchaineReunion
        print(f"Professeur {professeur.prenom} {professeur.nom} modifié avec succès.")
    else:
        print(f"Aucun professeur trouvé avec l'identifiant {identifiant}.")

def supprimerProfesseur():
    identifiant = int(input("Entrez l'identifiant du professeur à supprimer : "))
    if Professeur.supprimer(identifiant):
        print(f"Professeur avec identifiant {identifiant} supprimé avec succès.")
    else:
        print(f"Aucun professeur trouvé avec l'identifiant {identifiant}.")

def gestionProfesseurs():
    accueil("GESTION DES PROFESSEURS")
    while True:
        afficherSousMenuProf()
        try:
            choix = int(input("Choisissez une option dans le menu : "))
        except ValueError:
            print('Vous devez entrer un chiffre du menu !!')
            time.sleep(0.5)
            continue

        match choix:
            case 1:
                ajouterProfesseur()
            case 2:
                supprimerProfesseur()
            case 3:
                modifierProfesseur()
            case 4:
                listerProfesseurs()               
            case 5:
                break             
            case 0:
                return                   
            case _:
                print("Option invalide, veuillez réessayer !!")
                time.sleep(0.5)
                continue
