from flask import Flask, render_template,session,redirect
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'dlsjflkdjfljdsfj//..'

# database
client = MongoClient('mongodb+srv://maahin:admin@mongo-cluster.uc79axt.mongodb.net/?retryWrites=true&w=majority')
db_module = client.db

# routes
import user.models as model


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    if session.get('logged_in') != None:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/user/signup/', methods=['GET','POST'])
def signup():
    return model.User_class().signup()

@app.route('/user/signout/')
def signout():
    return model.User_class().signout()

@app.route('/user/login/', methods = ['POST'])
def login():
    return model.User_class().login()

if __name__ == '__main__':
    app.run(debug=True)