import dbServices as db
import configparser,time
from flask import Flask, render_template, request, session, jsonify

print('Hello Worlds')


#from FILE import file
app=Flask(__name__)
app.secret_key = 'the random string'
Registrants={}
Colors=['Silver', 'Blue','Green', 'Orange', 'Pink', 'Yellow','Violet','Majenta']


@app.route('/')
@app.route('/Sirs')
def index():
    return render_template('welcome.html')



@app.route('/abbu', methods=['post','get'])
def render():
        # return ('hello Mr Ajjulan')
    if (request.method  == 'GET'):
        grx_name =request.args.get('inp')
    elif ((request.method =='POST')):
        grx_name = request.form.get('user')
        print('grx name is:', grx_name)
        reg_id=db.write_to_reg_db(grx_name)
        session['gr_name'] = grx_name
        session['reg_id'] = reg_id
        print('@@@@@@@@Reg is is of type: ', type(session['reg_id']))
    #print('Input from browser is :', grx_name)

    return render_template('greet.html',pr_name=grx_name, t_colours=Colors)




@app.route('/showResults')
def showResultsPg():
    col=request.args.get('favColor')
    Registrants.update({session['gr_name']: col})
    choice_id=db.write_to_choice_db(session['reg_id'],col)
    print('Col= ',col ,' and ',session.get('gr_name'))
    #Registrants.append(kvp)
    return render_template('results.html', f_col=col,person=session.get('gr_name'))

@app.route('/addRegistrantsAPI')
def addRegistrantsAPI(newRegistrantName):
    reg_id=db.write_to_reg_db("Mha")
    return render_template('API_reg.html')





@app.route('/showRegistrants')
def showRegistrants():
    Registrants=db.read_from_db('choice', pWhr_Clause="INNER_JOIN")
    return render_template('registrants.html',RG=Registrants)


@app.route('/search')
def search():
        return render_template('search.html')


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/showRegistrantsAPI')
def showRegistrantsAPI():
    Registrants = db.read_from_db('choice', pWhr_Clause="INNER_JOIN")
    #data = ["DisneyPlus", "Netflix", "Peacock"]
#    print(json_string)
    val=({'name':'Jimit',
                    'address':'India'})
    return (jsonify(Registrants))

def setConfigs(filepath = r"./config/m7.config"):
    config = configparser.ConfigParser()
    print('The config to be read is:', filepath)
    #config.read('../config/company_lenovo.config')

    print("Here is the config file", config.read(filepath))
    print('The config file has these sections: ',config.sections())
    print('The DB name is: ', config.get("Database","DBName"))
    print('The Uid is: ', config.get("Database","uid"))

if __name__== '__main__':
    print('Today is :Sat')
    app.debug=True
    app.run(host="0.0.0.0", port=5005)
    #app.run(host="localhost", port=5003)
    #129.154.39.43 is the m3 on BalajeeIyer
    #app.run(host="129.154.39.43", port=5004)

