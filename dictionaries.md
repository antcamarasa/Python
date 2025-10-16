# Dictionnaire
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

Il est important de noter que les dictionnaires sont des collections de paires clé-valeur. Vous ne pouvez pas insérer une clé sans valeur correspondante, ni une valeur sans clé. Comme elles vont toujours de pair, vous devez insérer les deux simultanément.

💡 Remarque : Dans certains cas, vous pouvez vouloir ajouter des clés à un dictionnaire sans encore connaître la valeur associée.
Dans ces situations, vous pouvez utiliser la méthode .setdefault() pour créer des clés avec une valeur par défaut ou une valeur temporaire (placeholder).

En pratique, vous utiliserez un dictionnaire chaque fois que vous aurez besoin d’une structure de données mutable et efficace qui associe des clés à des valeurs.

--- 

### Créer des dictionnaires en Python
Vous pouvez créer des dictionnaires Python de plusieurs manières, selon nos besoins.

La methode la plus courante consiste a utiliser des littéraux de dictionnaire, c'est-à-dire une série de paire clé-valuer séparées par des virfules, entourées d'accolades {}.

La seconde methode consiste à utiliser le constructeur dict(), qui permet de créer des dictionnaires à partir :
- d'itérables contenant des paires clé-valeur.
- d'autres dictionnaires (ou mappings).
- ou encore d'une série d'arguments nommés (keyword arguments).

Vous pouvez aussi créer un dictionnaire vide en appelant dict() sans argument.

Nous allons voir en détail la création de dictionnaire a l'aide de littéreaux et du constructeur dict()

#### Litéraux de dictionnaire
Vous pouvez définir un dictionnaire en entourant une serie de paire clé-valeur par des acolades {}, chaque paire étant séparée par une virgule et chaque clé étant séparée de sa valeur par un deux-points (:).

Voici la syntaxe d'un littéral de dict : 

    {
      <clé_1>: <valeur_1>,
      <clé_2>: <valeur_2>,
      ...,
      <clé_N>: <valeur_N>,
    }

Les clés et les valeurs sont facultatives, ce qui signifie que vous pouvez simplement écrire {} pour créer un dictionnaire vide.

      my_dict = {}
      >>> On crée un dictionnaire vide, via le litéraux de dictionnaire

Chaque élément est une paire composée d’une clé, d’un deux-points et de la valeur associée. Les paires sont séparées par des virgules.

Les clés doivent être des objets hachables, comme des nombres, des chaînes de caractères ou des tuples.

Être hachable signifie que l’objet peut être passé à une fonction de hachage, qui transforme des données de taille arbitraire en une valeur de taille fixe, appelée valeur de hachage (hash). Cette valeur est utilisée pour les recherches et comparaisons dans une table de hachage.

Simplement, en Python, les types immuables sont hachables, tandis que les types mutables ne le sont pas.

💡 Remarque : Les ensembles (sets) utilisent également les accolades {}, mais pour contenir des éléments uniques, et non des paires clé-valeur. Pour créer un ensemble vide, il faut utiliser set() au lieu de {}, car cette dernière notation est réservée aux dictionnaires vides.

Exemple : dictionnaire de clubs de baseball
    
    >>> MLB_teams = {
    ...     "Colorado": "Rockies",
    ...     "Chicago": "White Sox",
    ...     "Boston": "Red Sox",
    ...     "Minnesota": "Twins",
    ...     "Milwaukee": "Brewers",
    ...     "Seattle": "Mariners",
    ... }

Ici, chaque clé correspond à une ville ou un État, et chaque valeur à une équipe de la MLB (Major League Baseball).

#### Clés hachables valides
Vous pouvez utiliser différents types d’objets hachables comme clés :

    >>> {
          42: "aaa",
          2.78: "bbb",
          True: "ccc",
    }

Vous pouvez même utiliser des types de données ou des fonctions comme clés :

    >>> types = {int: 1, float: 2, bool: 3}
    
    >>> print(types)
    {<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}

    >>> types[float]
    2

    >>> types[bool]
    3

#### Objets non hachables
Vous ne pouvez pas utiliser d’objets non hachables comme clés. Par exemple, les listes sont mutables et donc non hachables :

          >>> {[1, 2]: "Une liste comme clé ? Hmm..."}
          
          Traceback (most recent call last):
          ...
          
          TypeError: unhashable type: 'list'

Les listes ne sont pas hachables car si leur contenu changeait, leur valeur de hachage changerait aussi, ce qui violerait la règle selon laquelle le hash d’un objet doit rester constant. 

En pratique, vous ne pouvez donc pas utiliser de type mutable (liste, ensemble, dictionnaire) comme clé.


#### Utiliser des tuples comme clés

Si vous avez besoin d’utiliser des séquences comme clés, vous pouvez utiliser des tuples, car ils sont immuables :

          >>> a_dict = {(1, 1): "a", (1, 2): "b", (2, 1): "c", (2, 2): "d"}
          >>> a_dict[(1, 1)]
          'a'
          >>> a_dict[(2, 1)]
          'c'

Cependant, attention : un tuple contenant un objet mutable (comme une liste) n’est plus hachable :
        
        >>> {(1, [1, 1]): "a"}
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: 'list'

Car, un tuple est immuable mais les éléments que contient un tuple eux peuvent être mutable :
-  Un tuple de int,str,bool... est immuable.
- Un tupplue de list, dict... est immuable mais contient des objet mutables donc pas hashable.

#### Pas de doublons de clés
Les clés du dictionnaire doivent être uniques. Si vous assignez une valeur à une clé déjà existante, la valeur précédente est remplacée :

        >>> MLB_teams["Chicago"] = "Cubs"
        >>> MLB_teams
        {
          'Colorado': 'Rockies',
          'Chicago': 'Cubs',
          'Boston': 'Red Sox',
          'Minnesota': 'Twins',
          'Milwaukee': 'Brewers',
          'Seattle': 'Mariners',
        }

Ici, "Chicago": "White Sox" a été remplacé par "Chicago": "Cubs".


#### Valeurs de dictionnaire
Contrairement aux clés, les valeurs n’ont aucune restriction.
Elles peuvent être de n’importe quel type, y compris des objets mutables (listes, ensembles, dictionnaires) ou des objets personnalisés :

        >>> class Point:
        ...     def __init__(self, x, y):
        ...         self.x = x
        ...         self.y = y
        ...

        >>> {
        ...     "colors": ["red", "green", "blue"],
        ...     "plugins": {"py_code", "dev_sugar", "fasting_py"},
        ...     "timeout": 3,
        ...     "position": Point(42, 21),
        ... }

Dans cet exemple, le dictionnaire contient une liste, un ensemble, un entier, et un objet personnalisé.
Tout cela fonctionne car les valeurs n’ont aucune contrainte.

De plus, une même valeur peut apparaître plusieurs fois :

          >>> {0: "a", 1: "a", 2: "a", 3: "a"}
          {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
          
Ici, la valeur "a" est utilisée plusieurs fois, ce qui est parfaitement autorisé.

---

## Le constructeur dict()
Vous pouvez également construire des dictionnaires à l’aide du constructeur dict().
Les arguments de dict() peuvent être :
- Une série d’arguments nommés (keyword arguments) ;
- un autre dictionnaire (ou mappage) ;
- ou encore un itérable de paires clé–valeur.

Voici les différentes signatures possibles du constructeur :

    dict()
    dict(**kwargs)
    dict(mapping, **kwargs)
    dict(iterable, **kwargs)

Si on appel le constructeur dict(), sans argument, on obtient un dictionnaire vide :

      >>> dict()
          {}
Dans la plupart des cas, on utilise simplement une paire d’accolades vides {} pour créer un dictionnaire vide.

Cependant, dans certaines situations, utiliser le constructeur dict() peut rendre le code plus explicite.

#### Qu'est ce que **kwargs ? 

**kwargs sert à récupérer des arguments nommés (comme clé=valeur) dans une fonction.

kwargs signifie "keyword arguments", c’est-à-dire arguments nommés.
- ** indique que la fonction peut recevoir un nombre variable d'arguments nommés(sous forme de dictionnaire)
- le mot kwargs est une convention : On pourrait l'appeler (**params, par exemple) mais la norme est **kwargs

      def test(**kwargs):
        print(type(kwargs))
        print(kwargs)

      test(a=1, b=2)

      >>> <class 'dict'>
      >>> {'a': 1, 'b': 2}

🔹 Ici, kwargs n’est pas un dictionnaire que tu passes toi-même, mais Python le transforme en dictionnaire pour toi à l’intérieur de la fonction. C’est pour ça qu’on dit que kwargs se comporte comme un dictionnaire.

#### 🧱 4. Lien avec le constructeur dict(**kwargs)

Quand tu écris :

      d = dict(nom="Alice", age=30)
👉 Python passe en interne les arguments nommés sous forme de **kwargs à la fonction dict(), et dict() les transforme en un vrai dictionnaire :

      >>> {'nom': 'Alice', 'age': 30}

A la différence avec *args, pour les arguments positionnels.

#### 🧩 1. Signification de *args
- *args veut dire "arguments" (sans mots-clés).
- * indique que la fonction peut recevoir un nombre variable d’arguments positionnels,
- et les regroupe dans un tuple (un ensemble ordonné et immuable).

      def addition(*args):
        print(args)

      addition(1, 2, 3)

      >>> (1, 2, 3)

#### Exemple combine **kwargs et *args

    def demo(a, b, *args, **kwargs):
      print("a =", a)
      print("b =", b)
      print("args =", args)
      print("kwargs =", kwargs)

    demo(10, 20, 30, 40, 50, nom="Alice", age=30)

Resultat : 

      a = 10
      b = 20
      args = (30, 40, 50)
      kwargs = {'nom': 'Alice', 'age': 30}

- a et b → les deux premiers arguments normaux
- *args → tout ce qui reste sans nom
- **kwargs → tout ce qui reste avec un nom

### 1. Créer des dictionnaires avec les keyword arguments

Si les clés de votre dictionnaire sont des chaînes de caractères qui représentent des identifiants Python valides, vous pouvez les spécifier comme arguments nommés.
Voici un exemple avec un dictionnaire MLB_teams :

      >>> MLB_teams = dict(
      ...     Colorado="Rockies",
      ...     Chicago="White Sox",
      ...     Boston="Red Sox",
      ...     Minnesota="Twins",
      ...     Milwaukee="Brewers",
      ...     Seattle="Mariners",
      ... )

      # Output =>
      {
        'Colorado': 'Rockies',
        'Chicago': 'White Sox',
        'Boston': 'Red Sox',
        'Minnesota': 'Twins',
        'Milwaukee': 'Brewers',
        'Seattle': 'Mariners'
      }

Voyons pourquoi les clés ne sont pas entourées de guillemets, même si elles deviennent bien des chaînes de caractères dans le dictionnaire final.

Quand tu écris : 

      MLB_teams = dict(
      Colorado="Rockies",
      Chicago="White Sox",
      Boston="Red Sox"
      )

Python ,e voit pas ça comme des paire clé:valeur, mais comme des arguments nommés pass a la fonction dict().

Autrement dit, c'est exactement comme si on appelais une fonction classique :

      def ma_fonction(Colarado="Rockies", Chicago="White Sox")

Ici les noms Colorado, Chicago... sont des identifiants pythons, pas des chaines.
Mais lorsque dict() recoit ses arguments, Pythons les convertit automatiquement en clé de type str dans le dictionnaire.

#### Ce qu’il se passe sous le capot

Python fait ceci :
- Il lit tes arguments nommés (Colorado="Rockies", etc.)
- Il crée un dictionnaire interne :

      {"Colorado": "Rockies", "Chicago": "White Sox", "Boston": "Red Sox"}

- Il passe ce dict à dict(**kwargs)
- Le constructeur dict() crée ton vrai dictionnaire à partir de ça.

#### ⚠️ Limitation importante

Cette syntaxe ne marche que si les clés sont des identifiants Python valides :
- Pas d’espaces ("New York" ❌)
- Pas de tirets ("Los-Angeles" ❌)
- Pas de chiffres au début ("2Pac" ❌)
- Pas de caractères spéciaux ("Café" ❌ si accent non géré)

--- 

### 2. Créer un dictionnaire à partir d’un itérable de paires clé–valeur

Vous pouvez aussi créer un dictionnaire à partir d’un itérable de paires (clé, valeur). Voici comment construire le même dictionnaire MLB_teams de cette manière

    >>> MLB_teams = dict(
    ...     [
    ...         ("Colorado", "Rockies"),
    ...         ("Chicago", "White Sox"),
    ...         ("Boston", "Red Sox"),
    ...         ("Minnesota", "Twins"),
    ...         ("Milwaukee", "Brewers"),
    ...         ("Seattle", "Mariners"),
    ...     ]
    ... )

  Résultat :

      {
        'Colorado': 'Rockies',
        'Chicago': 'White Sox',
        'Boston': 'Red Sox',
        'Minnesota': 'Twins',
        'Milwaukee': 'Brewers',
        'Seattle': 'Mariners'  
      }

Dans cet exemple, vous construisez le dictionnaire à partir d’une liste de tuples contenant deux éléments :
- le premier est la clé, le second est la valeur associée.


### 3. Combiner zip() et dict()

Une méthode élégante pour créer des dictionnaires à partir de deux séquences consiste à utiliser la fonction intégrée zip(), puis à appeler dict() :


          >>> places = [
          ...     "Colorado",
          ...     "Chicago",
          ...     "Boston",
          ...     "Minnesota",
          ...     "Milwaukee",
          ...     "Seattle",
          ... ]

          >>> teams = [
          ...     "Rockies",
          ...     "White Sox",
          ...     "Red Sox",
          ...     "Twins",
          ...     "Brewers",
          ...     "Mariners",
          ... ]

          >>> dict(zip(places, teams))
          {
          'Colorado': 'Rockies',
          'Chicago': 'White Sox',
          'Boston': 'Red Sox',
          'Minnesota': 'Twins',
          'Milwaukee': 'Brewers',
          'Seattle': 'Mariners'
        }

La fonction zip() prend un ou plusieurs itérables en argument et renvoie des tuples combinant les éléments de chaque itérable.

🧠 Remarque importante :
Vos données d’origine doivent être ordonnées dans le bon ordre, car zip() associe les éléments position par position. Sinon, vous risquez d’obtenir un dictionnaire qui associe les mauvaises clés aux mauvaises valeurs.


### La methode fromkeys() 
Le type dict possède une méthode de classe appelée .fromkeys(), qui permet de créer un nouveau dictionnaire à partir :
- d’un itérable de clés,
- et d’une valeur par défaut.

Sa signature est la suivante :

          dict.fromkeys(iterable, value=None)

          iterable : contient les clés que vous voulez inclure dans le dictionnaire.
          Même si cet itérable contient des doublons, le dictionnaire final aura des clés uniques (comme toujours).

          value : permet de définir une valeur par défaut pour toutes les clés.
          Si vous ne précisez rien, la valeur par défaut sera None.

          >>> inventory = dict.fromkeys(["apple", "orange", "banana", "mango"], 0)
          
          >>> inventory
          {'apple': 0, 'orange': 0, 'banana': 0, 'mango': 0}

---

## 🔹 Accéder aux valeurs d’un dictionnaire
Une fois que vous avez créé un dictionnaire, vous pouvez accéder à son contenu en utilisant ses clés.
Pour récupérer une valeur à partir d’un dictionnaire, il suffit d’indiquer la clé correspondante entre crochets ([]) après le nom du dictionnaire :

      >>> MLB_teams["Minnesota"]
      'Twins'

      >>> MLB_teams["Colorado"]
      'Rockies'

Autrement dit, vous pouvez indexer (subscript) un dictionnaire avec une clé spécifique pour obtenir la valeur associée.

✅ La recherche d’une clé dans un dictionnaire est une opération très efficace, car les dictionnaires en Python sont implémentés sous la forme de tables de hachage (hash tables).



#### ⚠️ Clé inexistante

Si vous essayez d’accéder à une clé qui n’existe pas dans le dictionnaire,

Python lève une exception :

      >>> MLB_teams["Indianapolis"]
      Traceback (most recent call last):
      ...
      
      KeyError: 'Indianapolis'
      
➡️ Autrement dit, lorsqu’on tente d’accéder à une clé absente, Python déclenche une erreur KeyError.

#### 🔹 Exemple : dictionnaire imbriqué

Supposons maintenant que vous ayez le dictionnaire suivant contenant les données d’une personne :

      >>> person = {
      ...     "first_name": "John",
      ...     "last_name": "Doe",
      ...     "age": 35,
      ...     "spouse": "Jane",
      ...     "children": ["Ralph", "Betty", "Bob"],
      ...     "pets": {"dog": "Frieda", "cat": "Sox"},
      ... }

Ce dictionnaire contient :
- une liste comme valeur associée à la clé "children" ;
- un autre dictionnaire comme valeur associée à la clé "pets".

🔍 Accéder à une liste imbriquée

Pour accéder à un élément d’une liste contenue dans le dictionnaire, vous utilisez d’abord la clé correspondante, puis l’index souhaité :
      
      >>> person["children"][0]
      'Ralph'

      >>> person["children"][2]
      'Bob'

🐶 Accéder à un dictionnaire imbriqué

Pour accéder à une valeur à l’intérieur d’un dictionnaire imbriqué, vous utilisez la clé du dictionnaire extérieur, puis la clé intérieure :

    >>> person["pets"]["dog"]
    'Frieda'
    
    >>> person["pets"]["cat"]
    'Sox'

🧠 En résumé

Utiliser une clé pour accéder à une valeur dans un dictionnaire :
- dictionnaire["clé"]
- Utiliser clé + index pour accéder à une valeur dans une liste imbriquée.
- Utiliser clé extérieure + clé intérieure pour accéder à une valeur dans un dictionnaire imbriqué.
- Le niveau d’imbrication détermine combien de clés ou d’indices il faut enchaîner.
