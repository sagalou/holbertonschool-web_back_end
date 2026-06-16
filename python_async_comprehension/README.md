# Python - Async Comprehension

## Description

Ce projet fait partie du cursus back-end de Holberton School (`holbertonschool-web_back_end`, répertoire `python_async_comprehension`). Il porte sur les **comprehensions asynchrones** et les **générateurs asynchrones** en Python, introduits par la PEP 530.

## Objectifs d'apprentissage

À la fin de ce projet, vous devez être capable d'expliquer, sans aide extérieure :

- Comment écrire un générateur asynchrone
- Comment utiliser les comprehensions asynchrones
- Comment annoter le type d'un générateur

## Prérequis

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous les fichiers sont interprétés/compilés sur Ubuntu 20.04 LTS avec `python3` (version 3.8)
- Tous les fichiers se terminent par une nouvelle ligne
- La première ligne de chaque fichier est exactement `#!/usr/bin/env python3`
- Le code respecte le style `pycodestyle` (version 2.5.x)
- Toutes les fonctions et coroutines sont annotées avec leurs types
- Tous les modules et fonctions ont une documentation (vraies phrases explicatives)

## Ressources

- [PEP 530 -- Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What's New in Python: Asynchronous Comprehensions / Generators](https://blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-can-i-type-hint-a-generator-in-python-3)

## Tâches

### 0. Async Generator — `0-async_generator.py`

Coroutine `async_generator` qui boucle 10 fois, attend 1 seconde de manière asynchrone à chaque tour, puis génère (`yield`) un nombre aléatoire entre 0 et 10.

```bash
$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, ...]
```

### 1. Async Comprehensions — `1-async_comprehension.py`

Coroutine `async_comprehension` qui collecte 10 nombres aléatoires en utilisant une comprehension asynchrone sur `async_generator`, puis renvoie cette liste de 10 nombres.

```bash
$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, ...]
```

### 2. Run time for four parallel comprehensions — `2-measure_runtime.py`

Coroutine `measure_runtime` qui exécute `async_comprehension` quatre fois en parallèle grâce à `asyncio.gather`, mesure le temps total d'exécution, et le renvoie. Le temps total est d'environ 10 secondes : bien que les 4 appels soient lancés en parallèle, chacun contient sa propre boucle de 10 itérations avec 1 seconde d'attente à chaque tour, et ces attentes se chevauchent entre les 4 exécutions concurrentes au lieu de s'additionner.

```bash
$ ./2-main.py
10.021936893463135
```

## Auteur

Sagal Haider - [sagalou](https://github.com/sagalou)