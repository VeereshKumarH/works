from flask import Flask,render_template,request,redirect, url_for, session

app = Flask(__name__)
static_secret_key = 'veeresh'
app.secret_key = static_secret_key

@app.route('/')
@app.route('/login')
# @app.route('/login/<message>')
def login():
    message = request.args.get('message','')
    # message = message if message is not None else ''
    return render_template('login.html',message=message)

database = {'veer':'123','arun':'456'}
@app.route('/verify',methods=['POST','GET'])
def verify():
    username = request.form['username']
    password = request.form['password']
    if username not in database:
        # return render_template('login.html',message='Invalid User')
        return redirect(url_for('login',message='Invalid User'))    
    else:
        if database[username]!=password:
            # return render_template('login.html',message='Invalid Password')
            return redirect(url_for('login',message='Invalid Password'))
        else:
            # return render_template('home.html',user=username)
            session['username'] = username
            return redirect(url_for('home'))

@app.route('/home')
def home():
    username = session.get('username')
    return render_template('home.html',user=username)

@app.route('/facemaskclassifier')
def facemaskclassifier():
    return render_template('facemaskclassifier.html')

@app.route('/catdogclassifier')
def catdogclassifier():
    return render_template('catdogclassifier.html')

@app.route('/digitsclassifier')
def digitsclassifier():
    return render_template('digitsclassifier.html')

@app.route('/irisspeciesclassifier')
def irisspeciesclassifier():
    return render_template('irisspeciesclassifier.html')

@app.route('/titanicsurvivor')
def titanicsurvivor():
    return render_template('titanicsurvivor.html')

@app.route('/homepricepredictor')
def homepricepredictor():
    return render_template('homepricepredictor.html')

def create_app():
    return app