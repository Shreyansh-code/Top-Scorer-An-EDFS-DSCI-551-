from flask import Flask, render_template, request, redirect
import mysql.connector
import hdfs

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


@app.route('/templates/mkdir.html/')
def home1():
   return render_template('mkdir.html')


@app.route('/templates/ls.html/')
def home2():
   return render_template('ls.html')


@app.route('/templates/cat.html/')
def home3():
   return render_template('cat.html')


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


