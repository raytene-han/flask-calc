# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.get('/math/<operation>')
def view_all_in_one(operation):

    a = int(request.args["a"])
    b = int(request.args["b"])
    if operation == "add":
        result = add(a, b)
    elif operation == "sub":
        result = sub(a,b)
    elif operation == "mult":
        result = mult(a,b)
    elif operation == "div":
        result = div(a,b)
    return f"<html><body><h1>{result}</h1></body></html>"

@app.get('/add')
def view_add():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return f"<html><body><h1>{result}</h1></body></html>"

@app.get('/sub')
def view_sub():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return f"<html><body><h1>{result}</h1></body></html>"

@app.get('/mult')
def view_mult():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return f"<html><body><h1>{result}</h1></body></html>"

@app.get('/div')
def view_div():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return f"<html><body><h1>{result}</h1></body></html>"