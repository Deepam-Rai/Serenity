from re import L
from warnings import filters
from flask import request
from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
cors = CORS(app)

Diseases =  [{'Name':'Coivd-19','lab':['Dose1','Dose2','Booster']}]
patients = [{'Name':'Akash','Age':'23',"Gender":'Male','Diagnostic':'Covid-19','PP provider':'Aster','lab':['Dose1','Dose2','Booster']},{'Name':'Mrinal','Age':'24',"Gender":'Male','Diagnostic':'Covid-19','PP provider':'X Labs','lab':['Dose1']},{'Name':'Jammi Kunnal','Age':'21',"Gender":'Male','Diagnostic':'Covid-19','PP provider':'Aster','lab':['Dose1','Dose2','Booster']}]

@app.route('/login', methods=['GET', 'POST'])
def newaccount():
    if(request.method=='POST'):
        print("In The New Accoutn the recieved data is")
        uname = request.json['name']
        pswd  = request.json['pswd']
        if uname=='s' and pswd == 'S':
            return(jsonify({'output':'created'}))
        else:
            return(jsonify({'output':'UserNotFound'}))

@app.route('/search', methods=['GET', 'POST'])
def search():

    if(request.method=='POST'):
        user = request.json['name']
        gap = "empty"
        for i in patients:
            if i.get('Name') == user:
                print("Name Found")
                l = Diseases[0].get('lab')
                l1 = Diseases[0].get('lab').copy()
                print(l)
                print(i.get('lab'))
                for j in i.get('lab'):
                    if(j in l):
                        l1.remove(j)
                print(l1)
                gap=""
                for x in l1:
                    gap+=x+";"
        return(jsonify({'output':gap}))


