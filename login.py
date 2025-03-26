from flask import Flask, request, render_template, redirect
import os.path
from os import path

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])

def main():
    if request.method == "GET":     
        return render_template("Getinfo.html")
    else:
        return getinfo()
        return render_template('output.html')

@app.route('/info', methods = ["GET", "POST"])
def getinfo():
    global username, password
    username = request.form.get('txtUsername')
    password = request.form.get('txtpassword')
    if(username == "" or password == ""):
        return render_template('Getinfo.html')
    else:
        filename = username  + ".doc"
        Createfile(filename)
        return render_template('output.html', username = user, password = passtxt, status = status)
    
def Createfile(namefile):
    global status,user,passtxt
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filexist = bool(path.exists(namefile))
    
    if (filexist == False):
        locate = open(namefile, "x")
        locate.close()
        locate = open(namefile, "w")
        locate.write(username + "\n" + password)
        locate.close()
        status = "Username and password Created"
        retrieve(namefile)
    else:
        existing(namefile)

def retrieve(filename):
    global user,passtxt
    
    adminfile = open(filename,  "r")
    adminvalue = adminfile.read().splitlines()
    
    user = adminvalue[0].strip()
    passtxt = adminvalue[1].strip()

def existing(filename):
    global status,passtxt,user
    adminfile = open(filename,"r")
    adminvalue = adminfile.read().splitlines()
    
    passcheck = adminvalue[1].strip()

    if(password == passcheck):
        user = adminvalue[0].strip()
        passtxt = adminvalue[1].strip()
        status = "Username and Password Already exist!"
        adminfile.close()
    else:
        changepass(filename)
        
def changepass(namefile):
    global user
    global passtxt
    global status
    
    file = open(namefile, "w")
    file.write(username +"\n"+ password)
    file.close()
    status = "Password was changed"
    
    file = open(namefile,"r")
    filevalue = file.read().splitlines()
    user = filevalue[0].strip()
    passtxt = filevalue[1].strip()
    file.close()
    
if __name__ == "__main__":
    app.run()
