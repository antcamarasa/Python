# Dictionnaire en Python
- [Premiers pas avec les dictionnaires en Python](#premiers-pas-avec-les-dictionnaires-en-python)
- [Créer des dictionnaires en Python](#créer-des-dictionnaires-en-python)
  - [Littéraux de dictionnaire](#littéraux-de-dictionnaire)
  - [Le constructeur dict()](#le-constructeur-dict)
  - [Utiliser la méthode de classe .fromkeys()](#utiliser-la-méthode-de-classe-fromkeys)
- [Accéder aux valeurs d’un dictionnaire](#accéder-aux-valeurs-dun-dictionnaire)
- [Remplir un dictionnaire de manière progressive](#remplir-un-dictionnaire-de-manière-progressive)
  - [Attribuer des clés manuellement](#attribuer-des-clés-manuellement)
  - [Ajouter des clés dans une boucle for](#ajouter-des-clés-dans-une-boucle-for)
  - [Construire des dictionnaires avec des compréhensions](#construire-des-dictionnaires-avec-des-compréhensions)
- [Explorer les méthodes de la classe dict](#explorer-les-méthodes-de-la-classe-dict)
  - [Récupérer des données depuis un dictionnaire](#récupérer-des-données-depuis-un-dictionnaire)
  - [Ajouter des paires clé-valeur et mettre à jour un dictionnaire](#ajouter-des-paires-clé-valeur-et-mettre-à-jour-un-dictionnaire)
  - [Supprimer des données d’un dictionnaire](#supprimer-des-données-dun-dictionnaire)
- [Utiliser les opérateurs avec les dictionnaires](#utiliser-les-opérateurs-avec-les-dictionnaires)
  - [Appartenance : in et not in](#appartenance-in-et-not-in)
  - [Égalité et inégalité : == et !=](#égalité-et-inégalité--et-)
  - [Union et union augmentée : | et |=](#union-et-union-augmentée--et-)
- [Utiliser les fonctions intégrées avec les dictionnaires](#utiliser-les-fonctions-intégrées-avec-les-dictionnaires)
  - [Vérifier la présence de valeurs vraies : all() et any()](#vérifier-la-présence-de-valeurs-vraies-all-et-any)
  - [Déterminer le nombre d’éléments d’un dictionnaire : len()](#déterminer-le-nombre-déléments-dun-dictionnaire-len)
  - [Trouver les valeurs minimales et maximales : min() et max()](#trouver-les-valeurs-minimales-et-maximales-min-et-max)
  - [Trier un dictionnaire par clés, valeurs ou éléments : sorted()](#trier-un-dictionnaire-par-clés-valeurs-ou-éléments-sorted)
  - [Faire la somme des valeurs d’un dictionnaire : sum()](#faire-la-somme-des-valeurs-dun-dictionnaire-sum)
- [Itérer sur les dictionnaires](#itérer-sur-les-dictionnaires)
  - [Parcourir un dictionnaire par ses clés](#parcourir-un-dictionnaire-par-ses-clés)
  - [Itérer sur les valeurs d’un dictionnaire](#itérer-sur-les-valeurs-dun-dictionnaire)
  - [Boucler à travers les éléments d’un dictionnaire](#boucler-à-travers-les-éléments-dun-dictionnaire)
- [Explorer les classes existantes similaires aux dictionnaires](#explorer-les-classes-existantes-similaires-aux-dictionnaires)
- [Créer ses propres classes similaires aux dictionnaires](#créer-ses-propres-classes-similaires-aux-dictionnaires)
- [Conclusion](#conclusion)


## [Premiers pas avec les dictionnaires en Python](#premiers-pas-avec-les-dictionnaires-en-python)
Les dictionnaires sont l’un des types de données intégrés les plus importants et utiles de Python.
Ils offrent une collection mutable de paires clé-valeur, permettant d’accéder et de modifier efficacement les valeurs à l’aide de leurs clés correspondantes.

            config = {
              "color": "green",
              "width": 42,
              "height": 100,
              "font": "Courier",
            }

            # Access a value throught its key
            config["color"]
            >>> "green"

            #Update a value 
            config["font"] = "Helvetica"
            
            print(config)
            {
              'color': 'green',
              'width': 42,
              'height': 100,
              'font': 'Helvetica'
            }

Un dictionnaire python est une collection de paire "clé-valeurs", ou chaque clé correspond a une valeur. Dans l'exemple:
- 'color' est une clés
et,
- 'green' et la valeur associé a cette clé.

Les dictionnaires sont une partie fondamentale de Python. On les retrouve derrière des concepts essentiels tels que les espaces de noms (namespaces) et les portées (scopes), comme on peut le constater avec les fonctions intégrées globals() et locals() :


        >>> globals()
        {
          '__name__': '__main__',
          '__doc__': None,
          '__package__': None,
          ...
        }

La fonction globals() renvoie un dictionnaire contenant des paires clé-valeur qui associent des noms aux objets présents dans votre portée globale actuelle.

Python utilise également des dictionnaires pour gérer l’implémentation interne des classes. Considérez l’exemple de classe suivant :

        >>>   class Number:
                def __init__(self, value):
                  self.value = value

        >>>   Number(42).__dict__
        {value : 42}
            
L’attribut spécial .__dict__ est un dictionnaire qui associe les noms des attributs à leurs valeurs correspondantes dans les classes et objets Python. Cette implémentation permet une recherche rapide et efficace des attributs et des méthodes dans le cadre de la programmation orientée objet.


Vous pouvez utiliser les dictionnaires pour résoudre de nombreuses tâches de programmation dans votre code Python. Ils sont particulièrement utiles pour traiter des fichiers CSV et JSON, interagir avec des bases de données, charger des fichiers de configuration, et bien plus encore.

Les dictionnaires en python possèdent les carractéristiques suivantes :
- Mutables : les valeurs d’un dictionnaire peuvent être modifiées directement.
- Dynamiques : ils peuvent grandir ou rétrécir selon les besoins.
- Efficaces : ils sont implémentés sous forme de tables de hachage, ce qui permet une recherche rapide des clés.
- Ordonnés : Depuis 3.7, les dictionnaires conservent l'ordre d'insertion des éléménts.

Les clés d’un dictionnaire sont soumises à quelques restrictions. Elles doivent être :
- Hashables : cela signifie que vous ne pouvez pas utiliser des objets non hachables, comme les listes, les dict, les set en tant que clé, car ce sont des structures mutables
- Unique : un dictionnaire ne peut pas contenir de clés en double.

Les types hachables : 
- int, float, str, bytes
- tuple (si tous ces élements sont hachables)
- frozenSet(set immuable)
- bool (sous-classe de int)
- instances d'objets personnalisés si leur classe definit/autorise __hash__ et reste immuable

En revanche, les valeurs d’un dictionnaire n’ont pas de restrictions.

Elles peuvent être de n’importe quel type Python, y compris d’autres dictionnaires, ce qui permet de créer des dictionnaires imbriqués (nested dictionaries).
