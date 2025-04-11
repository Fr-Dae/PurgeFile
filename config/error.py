# config/error.py

import logging
import os
from config.color import color_text  # Assurez-vous que color_text est bien importé depuis config/colors.py

# Créer le dossier PURGE si nécessaire
purge_folder = os.path.join(os.path.dirname(__file__), "PURGE")
os.makedirs(purge_folder, exist_ok=True)

# Fichier de log
log_file = os.path.join(purge_folder, "log.txt")

# Initialisation du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ajouter un handler pour les logs dans un fichier
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Ajouter un handler pour afficher dans la console (uniquement les infos importantes)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(message)s')  # Affichage simple sans timestamp dans la console
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

def log_info(message):
    """Logge un message d'information."""
    logger.info(message)  # Log dans le fichier log.txt avec timestamp
    print(color_text(message, "green"))  # Affichage coloré dans la console

def log_warning(message):
    """Logge un message d'avertissement."""
    logger.warning(message)  # Log dans le fichier log.txt avec timestamp
    print(color_text(message, "yellow"))  # Affichage coloré dans la console

def log_error(message):
    """Logge un message d'erreur."""
    logger.error(message)  # Log dans le fichier log.txt avec timestamp
    print(color_text(message, "red"))  # Affichage coloré dans la console
