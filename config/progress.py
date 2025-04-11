# config/progress.py

from tqdm import tqdm
import time

def progress_bar(total, description):
    """
    Fonction pour créer une barre de progression avec tqdm.
    :param total: Le nombre total d'éléments à traiter.
    :param description: La description de la barre de progression.
    :return: Une instance de tqdm.
    """
    return tqdm(total=total, desc=description)

def update_progress_bar(pbar, increment):
    """
    Fonction pour mettre à jour la barre de progression.
    :param pbar: La barre de progression (instance de tqdm).
    :param increment: Le nombre à ajouter à la barre de progression.
    """
    pbar.update(increment)

# Exemple d'utilisation
if __name__ == "__main__":
    total_files = 100  # Le nombre d'éléments à traiter
    pbar = progress_bar(total_files, "Traitement des fichiers")  # Crée la barre de progression

    # Simulation du traitement des fichiers
    for i in range(total_files):
        time.sleep(0.1)  # Simule un traitement
        update_progress_bar(pbar, 1)  # Met à jour la barre de progression

    pbar.close()  # Ferme proprement la barre de progression
