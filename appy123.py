from flask import Flask,session,request,redirect,url_for,render_template
import mysql.connector as conn

app=Flask(__name__)

host_val="localhost"
user_val="root"
pass_val="root"
db_val="welcome"

db=conn.connect(host=host_val,
user=user_val,
passwd=pass_val,
database=db_val)

cur=db.cursor()

app.secret_key="some"

@app.route("/")
def fun():
    return render_template("home.html")


@app.route("/login")
def func1():
    return render_template("login123.html")

@app.route("/login",methods=["POST"])
def fun2():
    db = conn.connect(host=host_val,
                      user=user_val,
                      passwd=pass_val,
                      database=db_val)

    cur = db.cursor()
    if request.method=="POST":
        session["Email"]=request.form["email"]
        data=request.form
        cur.execute("select*from users where email='{}'".format(data["email"]))
        x=cur.fetchall()
        if len(x)==0:
            cur.execute("insert into users(email,password) values('{}','{}')".format(data["email"],data["pass"]))
            db.commit()
            db.close()
            return render_template("success.html")
        else:
            return render_template("login123.html")

@app.route("/profile")
def func4():
    return render_template("message.html")

@app.route("/logout")
def func3():
    return render_template("logout.html")



app.run(port=5002)