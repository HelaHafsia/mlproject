import sys  # Module qui fournit des informations sur l'exécution actuelle (par exemple, le traceback).
from src.logger import logging  # Import du logger pour enregistrer les logs d'erreur.

def error_message_detail(error, error_detail: sys):
    """
    Fonction utilitaire pour formater un message d'erreur détaillé.

    Arguments:
    ----------
    - error : L'exception levée (par exemple, ValueError, KeyError, etc.).
    - error_detail : L'objet sys contenant les détails de l'erreur (comme le traceback).

    Retourne:
    ---------
    - Un message d'erreur formaté qui précise le fichier, la ligne et le message d'erreur.
    """

    # `exc_info()` retourne un tuple de trois valeurs:
    # 1️⃣ Le type de l'exception levée (par exemple, TypeError, ValueError, etc.).
    # 2️⃣ L'objet de l'exception lui-même.
    # 3️⃣ L'objet traceback qui contient le détail de l'erreur (le fichier, la ligne, le code exécuté, etc.).
    # exc_tb: Correspond au traceback, c'est l'objet qui contient l'historique de l'erreur.
    # On l'utilise pour récupérer :
    # Le fichier (exc_tb.tb_frame.f_code.co_filename)
    #Le numéro de ligne (exc_tb.tb_lineno)


    _, _, exc_tb = error_detail.exc_info()

    # On récupère le nom du fichier où l'erreur s'est produite
    file_name = exc_tb.tb_frame.f_code.co_filename

    # On construit le message d'erreur détaillé
    error_message = "Error occurred in Python script name [{0}] at line number [{1}] with error message [{2}]".format(
        file_name,         # Nom du fichier
        exc_tb.tb_lineno,  # Numéro de la ligne où l'erreur est survenue
        str(error)         # Message d'erreur

    )

    # On retourne le message d'erreur formaté
    return error_message


class CustomException(Exception):
    """
    Classe personnalisée pour capturer les exceptions avec un message détaillé.
    Hérite de la classe de base `Exception`.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Constructeur de la classe CustomException.

        Arguments:
        ----------
        - error_message : Le message d'erreur personnalisé fourni lors de l'appel.
        - error_detail : L'objet sys contenant les détails de l'erreur.
        """
        # Appel au constructeur parent (Exception)
        super().__init__(error_message)

        # On génère un message d'erreur détaillé en appelant la méthode `error_message_detail`
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Méthode spéciale qui permet de retourner le message d'erreur détaillé
        lorsqu'on imprime l'exception.
        """
        return self.error_message

# if __name__=="__main__":
#     try :
#         a=1/0
#     except Exception as e :
#         logging.info("Divided by zero")
#         raise CustomException (e,sys)
    
