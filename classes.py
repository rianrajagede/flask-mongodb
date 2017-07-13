from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateTask(FlaskForm):
    title = TextField('Task Title')
    shortdesc = TextField('Short Description')
    priority = IntegerField('Priority')
    create = SubmitField('Create')

class DeleteTask(FlaskForm):
    key = TextField('Task ID')
    title = TextField('Task Title')
    delete = SubmitField('Delete')

class UpdateTask(FlaskForm):
    key = TextField('Task Key')
    shortdesc = TextField('Short Description')
    update = SubmitField('Update')

class ResetTask(FlaskForm):
    reset = SubmitField('Reset')
