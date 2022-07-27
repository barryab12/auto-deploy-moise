#!/usr/bin/python3
import subprocess, gdown, os.path
from getpass import getpass
import platform

print('Vos informations GITLAB de connexion vous seront demandées.')
username = input('User: ')
password = getpass(prompt='Pass: ')

url_addons = "git clone https://{}:{}@gitlab.com/dev-odoo-14/addons.git".format(
    username, password)
url_docker_compose = "git clone https://github.com/barryab12/openmoise-docker.git"
filestore_link = "https://drive.google.com/uc?id=1jMHuiniqvX11xJAlUzZtHvZM0eJPHnFk"

print("-- Téléchargement des images et fichiers documents ... ")
if not os.path.isdir('filestore/'):
    gdown.download(filestore_link, 'filestore.zip', quiet=False)

print("-- Téléchargement des modules")
if not os.path.isdir('addons/'):
    subprocess.run(url_addons, shell=True)

print("-- Téléchargement des fichiers de configurations ")
subprocess.run(url_docker_compose, shell=True)
subprocess.run('mv openmoise-docker/* .', shell=True)
subprocess.run('rm -fr openmoise-docker/', shell=True)
if not os.path.isfile('filestore.zip'):
    subprocess.run('unzip filestore.zip', shell=True)
print("-- Suppression des fichiers ... ")
subprocess.run('rm -fr filestore.zip', shell=True)
print("-- Lancement des conteneurs")
if os.path.isfile('docker-compose.yml') or os.path.isfile(
        'docker-compose.yaml'):
    subprocess.run('docker-compose up -d', shell=True)
else:
    print('le fichier docker-compose est inexistant')
