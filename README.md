## Objectif
Le but de ce TP est d'exporter les metriques d'une application web Flask sous le format Prometheus 


## Étapes

### Étape 1 : Création du projet Flask 
Tout d'abord, nous allons créer un projet Flask simple pour l'utiliser dans ce TP. Voici les étapes à suivre pour créer un projet Flask :

1. Créer un nouveau répertoire pour le projet :

```bash
mkdir flask-metrics
cd flask-metrics
```

2. Créer un environnement virtuel pour le projet :

```bash
python -m venv .venv
```

3. Activer l'environnement virtuel :

```bash
source .venv/bin/activate
```

4. Installer Flask :

```bash
pip install Flask
```

5. Créer un fichier app.py avec le contenu suivant :

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


Ce code définit une application Flask simple qui renvoie une chaîne de caractères "Hello, World!" lorsqu'elle est accédée à la racine de l'application.

### Configuration de la collecte de métriques sous le format Prometheus

1. Ajoutez le module Flask-Prometheus à votre application Flask en exécutant la commande suivante :

```bash
pip install Flask-Prometheus
```

2. Puis, ajoutez-les lignes de code suivantes à votre fichier app.py pour configurer la collecte de métriques avec Prometheus :


