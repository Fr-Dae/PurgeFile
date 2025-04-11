# color.py
from colorama import init, Fore, Back

# Initialiser colorama
init(autoreset=True)

def color_text(text, color, bg_color=None):
    """
    Fonction pour appliquer une couleur à un texte.
    
    Args:
    - text (str): Le texte à colorier.
    - color (str): Le nom de la couleur à appliquer (par exemple: 'red', 'green', 'yellow').
    - bg_color (str): (optionnel) La couleur de fond à appliquer (par exemple: 'blue', 'yellow').
    
    Returns:
    - str: Le texte coloré avec la couleur spécifiée.
    """
    color_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Fore.RESET
    }

    bg_color_map = {
        "black": Back.BLACK,
        "red": Back.RED,
        "green": Back.GREEN,
        "yellow": Back.YELLOW,
        "blue": Back.BLUE,
        "magenta": Back.MAGENTA,
        "cyan": Back.CYAN,
        "white": Back.WHITE,
        "reset": Back.RESET
    }

    color_code = color_map.get(color, Fore.RESET)  # Si la couleur n'est pas trouvée, on applique le reset
    bg_color_code = bg_color_map.get(bg_color, Back.RESET) if bg_color else Back.RESET  # Appliquer le fond si spécifié

    return f"{color_code}{bg_color_code}{text}"
