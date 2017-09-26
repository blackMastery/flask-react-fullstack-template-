from flask import Flask, render_template, url_for
import random

app = Flask(__name__, static_folder="../static/dist",template_folder="../static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return get_hello()


@app.route("/h")
def bye():
    return "goodbye react"

def get_hello():
    greeting_list = ['hola','Hei','Salut','Hej']
    return random.choice(greeting_list)



if __name__ =="__main__":
    app.debug = True
    app.run()
