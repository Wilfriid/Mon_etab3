import time
from base import bd
from menu import afficher_menu, accueil, quitter,menu_principal
from service import gestion_eleves, gestion_professeurs, gestion_utilisateurs

# Fonction pour récupérer un utilisateur depuis la base de données
def recuperer_utilisateur(identifiant):
    connection = bd.create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT pseudo, mot_de_passe FROM utilisateurs WHERE pseudo = %s", (identifiant,))
        utilisateur = cursor.fetchone()
        cursor.close()
        connection.close()
        return utilisateur
    return None

debut = time.time()

accueil("BIENVENUE DANS L'APPLICATION ETAB v1.3")
while True:
    identifiant = input("Entrez votre identifiant : ")
    mot_de_passe = input("Entrez votre mot de passe : ")
    
    utilisateur_data = recuperer_utilisateur(identifiant)
    
    if utilisateur_data and mot_de_passe == utilisateur_data[1]:  
        print("Authentification réussie !!")
        accueil("BIENVENUE DANS L'APPLICATION ETAB v1.3")
        while True:
            menu_principal()
            try:
                choix = int(input("Choisissez une option dans le menu : "))
            except ValueError:
                print('Vous devez entrer un chiffre du menu !!')
                continue

            match choix:
                case 1:
                    gestion_eleves.gestionEleves()
                case 2:
                    gestion_professeurs.gestionProfesseurs()
                case 3:
                    gestion_utilisateurs.gestionUtilisateurs()
                case 0:
                    quitter(debut)     
                    break               
                case _:
                    print("Option invalide, veuillez réessayer !!")
                    continue
    else:
        print("Échec de l'authentification, veuillez vérifier les informations saisies !")
        continue
    break

