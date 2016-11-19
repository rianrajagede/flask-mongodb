from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField
import redis, json

# config system
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))
r = redis.StrictRedis(host='localhost', port=6379, db=0)

class CreateTask(Form):
    title = TextField('Task Title')
    priority = IntegerField('Priority')
    create = SubmitField('Create')

class DeleteTask(Form):
    key = TextField('Task Key')
    delete = SubmitField('Delete')

class UpdateTask(Form):
    key = TextField('Task Key')
    title = TextField('Task Title')
    priority = IntegerField('Priority')
    update = SubmitField('Update')

class ResetTask(Form):
    reset = SubmitField('Reset')

def createTask(form):
    title = form.title.data
    priority = form.priority.data

    # set auto-generated key
    r.set('T'+str(r.get('id')),'{"title":"'+str(title)+'","priority":"'+str(priority)+'"}')
    r.incr('id')
    return redirect('/')

def deleteTask(form):
    key = form.key.data
    r.delete(key)
    return redirect('/')

def updateTask(form):
    title = form.title.data
    priority = form.priority.data
    key = form.key.data

    # update by "reset"
    r.set(key,'{"title":"'+str(title)+'","priority":"'+str(priority)+'"}')
    return redirect('/')

def resetTask(form):
    r.flushall()
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

    # get all data
    keys = r.keys()
    val = {}
    for i in keys:
        if i!='id':
            val[i]=json.loads(r[i])

    return render_template('home.html', cform = cform, dform = dform, uform = uform, \
                keys = keys, val = val, reset = reset)

if __name__=='__main__':
    # set auto-generated key
    if(r.exists('id')==False):
        r.set('id','0')

    app.run(debug=True)
