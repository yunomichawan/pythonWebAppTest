from flask import Flask
from flask import request

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
# URL: /hello/<name>?message=Have%20a%20nice%20day
@app.route('/hello/<name>')
# 有効なURLクエリを登録する?
@app.route('/testCall')
def hello(name):
    # クエリパラメータ取得
    msg = request.args.get('message','')
    # Render the page
    return "Hello " + name + "! "+ msg + "."

# routeに登録したが表示される文字は変わらず
def testCall():
    return "これで実行される?"

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)