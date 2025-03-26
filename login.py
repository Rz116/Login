from flask import Flask, request, render_template, redirect
import os.path
from os import path

global whichfilename
whichfilename = "LoginAccounts.doc"
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
        Createfile()
        return render_template('output.html', username = username, password = password)
    
def Createfile():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filexist = bool(path.exists(whichfilename))
    if (filexist == False):
        status = "new"
    else:
        status = "Edit"

    Writefile(status)
    
def Writefile(whichstatus):
    if(whichstatus == "new"):
        locate = open(whichfilename, "x")
        locate.close()
        locate = open(whichfilename, "w")
    else:
        locate = open(whichfilename, "a")
    locate.write(username + "  " + password)

if __name__ == "__main__":
    app.run()
