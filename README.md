# Simple CRUD-Web using MongoDB and Flask

This is a simple example of Python Flask's usage as a simple "Task Manager".
The Database Management System is MongoDB. 
The python-MongoDB connector is PyMongo.

### Installation

#### Docker

Using Docker compose, you can run this using one command:

```bash
$ docker-compose up
```

It will run pip install and also pull mongodb container as requirement of this project. Then you can access `localhost:80` (yes it is in port 80 since in `docker-compose.yml` it exposed to host port 80, you can change it if you like!).

#### Old way

> Don't forget to install python 3 if you don't have it, because this project use python 3 syntax such as `print()` function.

First, you should [install MongoDB](https://docs.mongodb.com/manual/installation/)

then install all dependencies by running the following command:

```
$ sudo pip install -r requirements.txt
```

It will install Flask, Flask-WTF, and PyMongo.

### Usage

To run the program, first you should make sure MongoDB is running, start it using:

```
$ sudo service mongod start
```

then, run the program:

```
$ python run.py
```

Open your browser and go to `localhost:5000` to see the running program.

### External References:

 * [Nice PyMongo Tutorial](http://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/)