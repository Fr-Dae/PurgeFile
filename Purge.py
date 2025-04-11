# Purge.py

import os
import shutil
import sys
from tqdm import tqdm

# Ajouter le dossier config au chemin pour les imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))

from config.errors import log_error, log_info
from config.progress import progress_bar, update_progress_bar
from config.multithreading import execute_multithreaded

# Définir les extensions de ROMS à vérifier
ROM_EXTENSIONS = {
    "a26", "a52", "a78", "xex", "j64", "st", "bin",
    "fds", "nes", "smc", "sfc", "swc", "gba", "gb", "gbc", "sgb", "nds", "n64", "z64", "v64",
    "smd", "md", "gen", "sms", "gg", "32x", "cue", "chd",
    "iso", "pbp", "img",
    "zip", "7z", "neo", "fba", "mame", "pak",
    "dsk", "adf", "ipf", "pce", "sgx", "vb", "ws", "wsc", "z80", "tap", "prg",
    "d64", "crt", "x68", "cdi", "sc", "rom", "tvc", "pico", "sv", "j2me", "p8"
}

# Déterminer si un fichier est japonais (JP, Japan, Japon, etc.)
def is_japanese(file_name):
    return any(keyword in file_name.lower() for keyword in ["jp", "japan", "japon"])

# Déterminer si un fichier est européen (Europe, Eu) sans mentionner USA

def is_european(file_name):
    return any(keyword in file_name.lower() for keyword in ["eu", "europe"]) and "usa" not in file_name.lower()

# Déterminer si un fichier USA a un fichier Europe ou FR correspondant
def is_usa_with_fr_duplicate(file_name, fr_files):
    base_name = os.path.splitext(file_name)[0]
    return any(f"{base_name.replace('us', 'fr')}" in f for f in fr_files)

# Déplacer un fichier vers le dossier de purge tout en maintenant l'arborescence
def move_to_purge(src_path, input_folder, purge_folder, log_file):
    try:
        relative_path = os.path.relpath(src_path, input_folder)
        dest_path = os.path.join(purge_folder, relative_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        if not os.path.exists(dest_path):
            shutil.move(src_path, dest_path)
            with open(log_file, "a",encoding="utf-8") as log:
                log.write(f"Déplacé: {src_path} → {dest_path}\n")
        else:
            with open(log_file, "a") as log:
                log.write(f"Fichier déjà présent: {dest_path}\n")
    except Exception as e:
        log_error(f"Erreur lors du déplacement de {src_path}: {e}")

# Créer les dossiers RESULT et les sous-dossiers A-Z
def create_result_folders(result_folder):
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        folder_path = os.path.join(result_folder, letter)
        os.makedirs(folder_path, exist_ok=True)

# Fonction d'inspection du répertoire
def inspect_directory(input_folder, result_folder, purge_folder, log_file):
    fr_files = set()
    potential_duplicates = []
    total_files = sum(len(files) for _, _, files in os.walk(input_folder))

    log_info(f"Total de {total_files} fichiers à traiter.")

    for root, _, files in os.walk(input_folder):
        if "RESULT" in root or "PURGE" in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            lower_file = file.lower()

            first_letter = file[0].upper()
            if first_letter.isalpha():
                dest_folder = os.path.join(result_folder, first_letter)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))
                with open(log_file, "a") as log:
                    log.write(f"Déplacé: {file_path} → {dest_folder}/{file}\n")

            if is_japanese(file) or is_european(file):
                move_to_purge(file_path, input_folder, purge_folder, log_file)
                continue

            if "fr" in lower_file:
                fr_files.add(file)

            if any(keyword in lower_file for keyword in ["us", "usa"]):
                potential_duplicates.append(file_path)

            if any(file.endswith(f".{ext}") for ext in ROM_EXTENSIONS):
                zip_file = file.replace(file.split(".")[-1], "zip")
                if zip_file in files:
                    move_to_purge(file_path, input_folder, purge_folder, log_file)

    for us_file in potential_duplicates:
        if is_usa_with_fr_duplicate(os.path.basename(us_file), fr_files):
            move_to_purge(us_file, input_folder, purge_folder, log_file)

# Fonction principale
def main():
    input_folder = input("Entrez le chemin du dossier à inspecter : ").strip()
    if not os.path.isdir(input_folder):
        log_error("Chemin invalide.")
        return

    result_folder = os.path.join(input_folder, "RESULT")
    os.makedirs(result_folder, exist_ok=True)
    create_result_folders(result_folder)

    purge_folder = os.path.join(input_folder, "PURGE")
    os.makedirs(purge_folder, exist_ok=True)

    log_file = os.path.join(input_folder, "log.txt")
    if not os.path.exists(log_file):
        with open(log_file, "w") as log:
            log.write("Log de déplacement des fichiers\n")

    log_info(f"Inspection de {input_folder}...")

    files_to_process = [os.path.join(root, file) for root, _, files in os.walk(input_folder) for file in files]

    pbar = tqdm(total=len(files_to_process), desc="Traitement des fichiers", unit="fichier")

    def process_file(file_path):
        inspect_directory(input_folder, result_folder, purge_folder, log_file)
        pbar.update(1)

    execute_multithreaded(process_file, files_to_process)

    pbar.close()
    log_info("Inspection terminée.")

if __name__ == "__main__":
    main()
