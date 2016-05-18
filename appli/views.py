from flask import render_template
from appli import app

@app.route('/')
@app.route('/index')
def index():
    name = 'Victor'
    title = 'SysDev Blog'
    return render_template('index.html', name=name, title=title)
