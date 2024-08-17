from datetime import datetime
import time







def accueil():
    print("Bienvenue")
    



def menu_principal():
            print("\nMenu Principal :")
            print("1. Gérer les Élèves")
            print("2. Gérer les Professeurs")
            print("3. Gérer les Utilisateurs (À Venir)")
            print("4. Quitter")
            print(f"Date système : {datetime.datetime.now().strftime('%H:%M')}")
            
           

def menu_eleve():
            print("\nGestion des Élèves :")
            print("1. Ajouter un élève")
            print("2. Supprimer un élève")
            print("3. Mettre à jour un élève")
            print("4. Liste des élèves")
            print("5. Dernier élève ajouté")
            print("6. Retour au menu principal")



def afficherSousMenuProf():
    print("\n\tMENU")
    print("1: Ajouter un professeur")
    print("2: Supprimer un professeur")
    print("3: Modifier les informations du professeur")
    print("4: Lister les professeurs")
    print("5: Retour")    
    print("0: Accueil")

def afficherSousMenuUtil():
    print("\n\tMENU")
    print("1: Ajouter un utilisateur")
    print("2: Supprimer un utilisateur")
    print("3: Modifier les informations d'un utilisateur")
    print("4: Lister les utilisateurs")
    print("5: Retour")    
    print("0: Accueil")

def quitter(debut):
    fin = time.time()
    duree = fin - debut
    minutes, seconds = divmod(duree, 60)
    print("Merci d'avoir utilisé l'application ! À bientôt.")
    print(f"Durée de la session : {int(minutes)} minutes et {int(seconds)} secondes.")
