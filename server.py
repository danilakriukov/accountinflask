from flask import Flask, render_template, request
import time
from datetime import datetime

app = Flask(__name__)
elist = []

@app.route('/')
def first():
  return render_template("base.html")


@app.route('/second',methods=['POST','GET'])
def second():
 emotions = request.form['insertem']
 elist.append(emotions)
 return render_template("second.html",e=elist)


if __name__ == "__main__":
 app.run()