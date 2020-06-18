import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/wassup')
def wassup():
    return 'Nothing much, just doing some openshift stuff'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
