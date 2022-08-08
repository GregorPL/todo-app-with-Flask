from django.shortcuts import render
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/add_task')
def add_task():
    return render_template('add_task.html')