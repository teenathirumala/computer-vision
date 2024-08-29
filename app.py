# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, Flask!"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
app=Flask(__name__)
# this inshort creates WSGI applications:wsgi application is a standard that is actually used to communicate between the webserver and the web application that we are going to create

@app.route('/')
# decorator 
def intro():
    return "hello everyone.I am teena chowdary"

@app.route('/members')
def members():
    return "hello people.good afternoon"



if __name__=='__main__':
    app.run(debug=True)