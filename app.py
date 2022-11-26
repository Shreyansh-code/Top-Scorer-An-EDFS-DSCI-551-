from flask import Flask, render_template, request, redirect
import mysql.connector
import hdfs
import requests
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreyansh12"
)

cursor = db.cursor()


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/templates/mkdir/', methods=["GET", "POST"])
def home1():
    if request.method=="GET":
        return render_template('mkdir.html', done=False)
    elif request.method=="POST":
        name = request.form.get("name")
        cursor.execute("use dsci551")
        cursor.execute("insert into namenode3 (path, name, fileType) values('root/{0}', '{1}', 'dir')".format(name, name))
        db.commit()
        return render_template('mkdir.html', done=True)


@app.route('/templates/ls/')
def home2():
    cursor.execute("use dsci551")
    cursor.execute("select path from namenode3")
    lslist = []
    for x in cursor:
        lslist.append(x)
    return render_template('ls.html',lslist=lslist)


@app.route('/templates/cat/', methods=["GET", "POST"])
def home3():
    if request.method=="GET":
        return render_template('cat.html', done=False)
    
    if request.method=="POST":
        name = request.form.get("name")
        df= pd.read_csv('{}.csv'.format(name))
        return render_template('df.html', df=df.values)


@app.route('/templates/upload.html/')
def home4():
   return render_template('upload.html')


if __name__ == '__main__':
   app.run()





# @app.route("/")
# def main():
#     # cars = []
#     # cursor.execute("use dsci551")
#     # cursor.execute("SELECT * FROM namenode3")
#     # for row in cursor.fetchall():
#     #     cars.append({"id": row[0], "path": row[1], "name": row[2], "fileType": row[3]})
#     # db.commit()
#     # cursor.close()

#     return render_template("index.html")


