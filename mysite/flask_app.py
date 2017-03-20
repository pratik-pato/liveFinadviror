import src.sql as sql
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/finadvisor')
def home():
    return flask.render_template('login.html')
    #return 'Hello from Flask!'

@app.route('/finadvisor/register',methods = ['GET','POST'])
def register():
    return flask.render_template('register.html')

@app.route('/finadvisor/register/insert',methods = ['GET','POST'])
def dump():
        if flask.request.method == 'POST':
            formData = []
            result = flask.request.form
            formData.append(result['userName'])
            formData.append(result['contact'])
            formData.append(result['firstName'])
            formData.append(result['middleName'])
            formData.append(result['lastName'])
            formData.append(result['password'])
            formData.append(result['email'])
            #print formData
            if sql.consultantInsert(formData) == 1:
                return "<h1>ERROR IN DATA</h1>"
            #print formData[1]
            else:
                return "<h1>CONSULTANT REGISTERED</h1>"
                #return flask.render_template('result.html',result = result)
