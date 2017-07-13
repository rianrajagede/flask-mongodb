from flask import Flask, render_template, redirect
from pymongo import MongoClient
from classes import *

# config system
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))
client = MongoClient('localhost:27017')
db = client.TaskManager

if db.settings.find({'name': 'task_id'}).count() <= 0:
    print("task_id Not found, creating....")
    db.settings.insert_one({'name':'task_id', 'value':0})

def updateTaskID(value):
    task_id = db.settings.find_one()['value']
    task_id += value
    db.settings.update_one(
        {'name':'task_id'},
        {'$set':
            {'value':task_id}
        })

def createTask(form):
    title = form.title.data
    priority = form.priority.data
    shortdesc = form.shortdesc.data
    task_id = db.settings.find_one()['value']
    
    task = {'id':task_id, 'title':title, 'shortdesc':shortdesc, 'priority':priority}

    db.tasks.insert_one(task)
    updateTaskID(1)
    return redirect('/')

def deleteTask(form):
    key = form.key.data
    title = form.title.data

    if(key):
        print(key, type(key))
        db.tasks.delete_many({'id':int(key)})
    else:
        db.tasks.delete_many({'title':title})

    return redirect('/')

def updateTask(form):
    key = form.key.data
    shortdesc = form.shortdesc.data
    
    db.tasks.update_one(
        {"id": int(key)},
        {"$set":
            {"shortdesc": shortdesc}
        }
    )

    return redirect('/')

def resetTask(form):
    db.tasks.drop()
    db.settings.drop()
    db.settings.insert_one({'name':'task_id', 'value':0})
    return redirect('/')

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    cform = CreateTask(prefix='cform')
    dform = DeleteTask(prefix='dform')
    uform = UpdateTask(prefix='uform')
    reset = ResetTask(prefix='reset')

    # response
    if cform.validate_on_submit() and cform.create.data:
        return createTask(cform)
    if dform.validate_on_submit() and dform.delete.data:
        return deleteTask(dform)
    if uform.validate_on_submit() and uform.update.data:
        return updateTask(uform)
    if reset.validate_on_submit() and reset.reset.data:
        return resetTask(reset)

    # read all data
    docs = db.tasks.find()
    data = []
    for i in docs:
        data.append(i)

    return render_template('home.html', cform = cform, dform = dform, uform = uform, \
            data = data, reset = reset)

if __name__=='__main__':
    app.run(debug=True)
