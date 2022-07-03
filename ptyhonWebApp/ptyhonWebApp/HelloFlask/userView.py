from datetime import datetime
from flask import render_template,request
from HelloFlask import app

@app.route('/')
@app.route('/login')
def login():
    return render_template(
        "userView/login.html")

@app.route('/',methods=['GET','POST'])
def loginhome():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    id = ''
    if request.method == 'POST':
        id = request.form['id']

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)

@app.route('/userView')
def userView():
    return render_template(
        "userView/folderPage.html")
