from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/userView')
def userView():
    return render_template(
        "userView/folderPage.html")
