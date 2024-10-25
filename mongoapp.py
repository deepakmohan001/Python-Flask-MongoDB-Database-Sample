from flask import Flask,render_template,url_for,request,redirect
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient('localhost',27017)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user_collection.insert_one({'username':username,'password':password})
        return redirect(url_for('user_list'))
    return render_template('index1.html')

@app.route('/users',methods=['GET'])
def user_list():
    all_users = user_collection.find()
    return render_template('login.html', users=all_users)





# Mongo Database
db=client.flask1_database

# collection
user_collection=db.user

if __name__=='__main__':
    app.run(debug=True)
















