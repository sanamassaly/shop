# 🛒 Shop - Plateforme E-commerce Django

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.x-green)](https://www.django-project.com/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Une plateforme e-commerce moderne développée avec Django, offrant une expérience d'achat complète.

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)
- Git (pour cloner le projet)

## 🚀 Installation Rapide

### 1. Cloner le projet

git clone https://github.com/sanamassaly/shop.git
cd shop

### 2. Créer un environnement virtuel
# Pour Windows
python -m venv venv
venv\Scripts\activate

# Pour Linux/Mac
python3 -m venv venv
source venv/bin/activate

### 3. Installer les dépendances
pip install -r requirements.txt

### 4. Appliquer les migrations
python manage.py migrate

### 5. Créer un superutilisateur
python manage.py createsuperuser
Suivez les instructions pour définir :

Nom d'utilisateur

Adresse email

Mot de passe

### 6. Lancer le serveur de développement
python manage.py runserver

Accédez à l'application :

🌐 Site : http://127.0.0.1:8000/

🔧 Admin : http://127.0.0.1:8000/admin/
