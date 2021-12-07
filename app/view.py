from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db
  
  
@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
  
    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/addItem', methods=['POST'])
def addItem():
	todo = Todo(text=request.form['todoitem'],complete=False)
	db.session.addItem(todo)
	db.session.commit()
	return redirect(url_for('index'))