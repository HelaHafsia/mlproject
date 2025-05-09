import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Exemple de résultat : `05_07_2025_14_30_22.log` si le script est exécuté le 7 mai 2025 à 14h30min22s.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# - `os.path.join()` construit un chemin propre dans le chemin actuelle d'execution 
# en ajoutant un dossier "logs" et le nom du fichier log.

os.makedirs(logs_path,exist_ok=True)
# - `os.makedirs()` permet de créer un répertoire.
# - `exist_ok=True` évite une erreur si le répertoire existe déjà.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
# - Ici, `LOG_FILE_PATH` correspond au chemin complet vers le fichier `.log`

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# ✨ **Format des logs expliqué :**
# - `%(asctime)s`   : Affiche la date et l'heure de l'événement.
# - `%(lineno)d`    : Affiche le numéro de ligne où le log a été généré.
# - `%(name)s`      : Le nom du module ou logger.
# - `%(levelname)s` : Le niveau de sévérité (INFO, DEBUG, ERROR...).
# - `%(message)s`   : Le message proprement dit.

# Exemple de ligne de log générée :
# [2025-05-07 14:30:22,512] 15 root - INFO - logging has started

# if __name__=="__main__":
#     logging.info("logging has started")