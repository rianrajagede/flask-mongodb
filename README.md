# Simple CRUD-Web using MongoDB and Flask

This is a simple example of Python Flask's usage as a simple "Task Manager".
The Database Management System is MongoDB. 
The python-MongoDB connector is PyMongo.

### Installation

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

Open your browser and go to `localhost:5000	` to see the running program.

### External References:

 * [Nice PyMongo Tutorial](http://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/)