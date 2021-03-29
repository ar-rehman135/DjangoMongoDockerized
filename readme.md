## **********This is a Django Project***********

    Django REST Project with MOngo Database Engine and Dockerized.

    This project is being Dockerized into a Docker.


## Required Modules are written in 'requirements.txt' file


## To start this project from Ubuntu Terminal:

    Go to the root folder of your project where the docker files and manage.py exist from your terminal.

## To run using VScode or Pycharm

## To run throught Docker:

    $ docker-compose build
    $ docker-compose up

## To run thought local server:

    $ python3 manage.py runserver

## To migrate your project:

    $ python3 manage.py migrate

## To create a superuser of your admin:

    $ python3 manage.py createsuperuser

## Note: If you get MongOdb ERROR.

## You can Install it by the following Command from your terminal:
    
    $ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

## if you receive an error indicating that gnupg is not installed, you can:

    $ sudo apt-get install gnupg

## Once installed, retry importing the key:

    $ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

## Create the /etc/apt/sources.list.d/mongodb-org-4.4.list file for Ubuntu 18.04 (Bionic):

    $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

## Reload local package database:

    $ sudo apt-get update

## To install the latest stable version, issue the following:

    $ sudo apt-get install -y mongodb-org

## Start MongoDB:

    $ sudo systemctl start mongod

    $ sudo systemctl daemon-reload

## Verify that MongoDB has started successfully:

    $ sudo systemctl status mongod

    $ sudo systemctl enable mongod
    
## Begin using MongoDB:

    $ Mongo


