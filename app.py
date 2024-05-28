from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__ ,template_folder = 'template')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/food'
db = SQLAlchemy(app)

class Foodinfo(db.Model):
    # table contents in phpyhome = sno,name,email,phone,time
    #unique reprents if name should be unique
    #nullable true means field can be blank
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(26), unique=False, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=False)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html') 

@app.route('/bookings',methods = ['POST', 'GET'])
def bookings():
     if request.method == 'POST':
        # Add Entry To The DataBase
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        #fetched in variables
        # database ke column ka variable = upar vale varibale ko set karna
        # print(name,email,phone)
        entry = Foodinfo(name=name,email=email,phone=phone)
        db.session.add(entry)
        db.session.commit()
     return render_template('bookings.html') 

if __name__ == "__main__":
    app.run(debug=True)
  