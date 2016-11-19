# Simple CRUD-Web using REDIS and Flask

This is a simple example of Python Flask's usage as a simple "Task Manager" using Redis as Database Management System.

> **NOTE** : It works only on Ubuntu

### Installation

run this following command:

```
$ sudo pip install -r requirements.txt
```

It will install Flask, Flask-WTF, and Redis.

### Usage

To run the program, first you should run the redis-server:

```
$ redis-server
```

then, run the program:

```
$ python run.py
```

Open your browser and go to `localhost:5000	` to see the running program.

### References:

 * [Redis-py](https://github.com/andymccurdy/redis-py)
 * [Redis-py Documentation](https://redis-py.readthedocs.io/en/latest/)
