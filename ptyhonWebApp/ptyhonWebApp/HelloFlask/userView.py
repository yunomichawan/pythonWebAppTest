from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/userView')
def userView():
    return render_template(
        "userView/folderPage.html")


# 引数で表示するページを変えたい
@app.route('/process1')
def process():
    return render_template(
        "userView/Process1.html")