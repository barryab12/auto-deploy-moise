#!/usr/bin/python3
from genericpath import isdir
import platform, wget
import subprocess, os.path
from getpass import getpass
from zipfile import ZipFile

print('Vos informations GITLAB de connexion vous seront demandées.')
username = input('User: ')
password = getpass(prompt='Pass: ')

url_addons = "git clone https://{}:{}@gitlab.com/dev-odoo-14/addons.git".format(
    username, password)
url_docker_compose = "git clone https://github.com/barryab12/openmoise-docker.git"
filestore_url = 'https://filestoremoise.s3.amazonaws.com/filestore.zip'

print("-- Téléchargement des images et fichiers documents ... ")
if not os.path.isdir('filestore/') or not os.path.isfile('filestore.zip'):
    wget.download(filestore_url)

print("-- Téléchargement des modules")
if not os.path.isdir('addons/'):
    subprocess.run(url_addons, shell=True)

print("-- Téléchargement des fichiers de configurations ")
subprocess.run(url_docker_compose, shell=True)
if (platform.system() == "Linux"):
    subprocess.run('mv openmoise-docker/* .', shell=True)
elif (platform.system() == "Windows"):
    subprocess.run('move .\openmoise-docker\* .', shell=True)
if (platform.system() == "Linux"):
    subprocess.run('rm -fr openmoise-docker/', shell=True)
elif (platform.system() == "Windows"):
    subprocess.run('del openmoise-docker\ ', shell=True)
print('Extraction des fichiers et documents en cours ...')
if not os.path.isdir('filestore'):
    # with ZipFile('filestore.zip', 'r') as file:
    #     file.extractall()
    if (platform.system() == "Linux"):
        subprocess.run('unzip filestore.zip', shell=True)
    elif (platform.system() == "Windows"):
        print('Dezipper manuellement le fichier filestore.zip')

print("-- Suppression des fichiers ... ")
if os.path.isdir('filestore'):
    if (platform.system() == "Linux"):
        subprocess.run('rm -fr filestore.zip', shell=True)
    elif (platform.system() == "Windows"):
        subprocess.run('del filestore.zip', shell=True)
print("-- Lancement des conteneurs")
if os.path.isfile('docker-compose.yml') or os.path.isfile(
        'docker-compose.yaml'):
    subprocess.run('docker-compose up -d', shell=True)
else:
    print('le fichier docker-compose est inexistant')
