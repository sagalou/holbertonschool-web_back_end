# Python - Async Function

## Description

Ce projet fait partie du cursus back-end de Holberton School (`holbertonschool-web_back_end`, répertoire `python_async_function`). Il porte sur la programmation asynchrone en Python avec le module `asyncio` : coroutines, syntaxe `async`/`await`, exécution concurrente, et création de tâches (`asyncio.Task`).

## Objectifs d'apprentissage

À la fin de ce projet, vous devez être capable d'expliquer, sans aide extérieure :

- La syntaxe `async` et `await`
- Comment exécuter un programme asynchrone avec `asyncio`
- Comment lancer des coroutines en concurrence
- Comment créer des tâches `asyncio`
- Comment utiliser le module `random`

## Prérequis

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous les fichiers sont interprétés/compilés sur Ubuntu 20.04 LTS avec `python3` (version 3.8)
- Tous les fichiers se terminent par une nouvelle ligne
- La première ligne de chaque fichier est exactement `#!/usr/bin/env python3`
- Le code respecte le style `pycodestyle` (version 2.5.x)
- Toutes les fonctions et coroutines sont annotées avec leurs types (compatibles Python 3.8)
- Tous les modules, classes et fonctions ont une documentation (vraies phrases explicatives)
- Tous les fichiers sont exécutables

## Ressources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Tâches

### 0. The Basics of Async — `0-basic_async_syntax.py`

Coroutine asynchrone `wait_random` qui prend en argument un entier `max_delay` (valeur par défaut `10`), attend un délai aléatoire (float) compris entre `0` et `max_delay` secondes, puis renvoie ce délai.

```bash
$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

### 1. Let's execute multiple coroutines at the same time with async — `1-concurrent_coroutines.py`

*(à venir)*

## Auteur

Sagal Haider - [sagalou](https://github.com/sagalou)
