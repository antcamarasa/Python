"""
🧠 Comprendre la récursion et la gestion de la profondeur (level) dans un dictionnaire imbriqué

🎯 Objectif : 
-> Afficher chaque clé et son niveau d’imbrication dans un dictionnaire potentiellement imbriqué.



⚙️ 1. Version de base — passage du niveau par valeur

def search_key_in_dict_nested(d: dict):

    def helper_recursive(d, level):
        for k, v in d.items():
            current_level = level
            if not isinstance(v, Mapping):
                print(f"Level : {current_level} key : {k}")
            else:
                print(f"Level : {current_level} key : {k}")
                helper_recursive(v, current_level + 1)

    helper_recursive(d, 0)

🔍 Compréhension

helper_recursive(v, current_level + 1) passe une nouvelle valeur du niveau à chaque appel.

Chaque appel récursif crée une nouvelle frame (contexte d’exécution).

Le level du parent n’est jamais modifié :
il reste identique quand on revient de la récursion.

👉 Ici, level + 1 est une simple expression : elle calcule une valeur sans affecter la variable level dans la frame actuelle.

🧩 Schéma de frames

"""