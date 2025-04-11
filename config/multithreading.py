# config/multithreading.py

import concurrent.futures
import os

def execute_multithreaded(func, args_list, max_threads=None):
    """
    Exécute une fonction en multithread avec un nombre maximal de threads.
    :param func: La fonction à exécuter.
    :param args_list: Liste d'arguments à passer à la fonction.
    :param max_threads: Nombre maximal de threads à utiliser.
    :return: Une liste de résultats de la fonction.
    """
    if max_threads is None:
        max_threads = os.cpu_count() * 0.75  # Utiliser 75% des CPU par défaut

    max_threads = max(1, int(max_threads))  # Ne jamais avoir moins d'un thread

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        try:
            results = list(executor.map(func, args_list))
        except Exception as e:
            print(f"Une erreur est survenue lors de l'exécution en multithread: {e}")

    return results
