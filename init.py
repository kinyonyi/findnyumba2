from flask import Flask, render_template, request, url_for, flash, redirect
import db
app = Flask(__name__)
app.secret_key = 'my_app'

#first route for the login
@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        flash ( 'Welcome, please provide login credentials', 'info')
        #print(x)
        return render_template('login.html')
    else:
        uname = request.form['username']
        pword = request.form['password']
        x = db.query_login_registered()
        if (uname, pword) in x.items():
            print(x)
            return redirect(url_for('upload_page'))
        else:
            flash ( 'Invalid login credentials for Username' + ': ' + uname + ' and Password: '+ pword, 'error')
            print(x)
            return redirect(url_for('login'))

#second route for the registration
@app.route('/register', methods = ['POST', 'GET'])
def Register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        date = request.form['date']
        email = request.form['email']
        password = request.form['password']
        verify_password = request.form['password2']
        if password == verify_password and len(password) >= 4:
            db.create_table_register()
            db.insert_registered(firstname = firstname, lastname =lastname, username = username, date = date, email = email, password = password, table_name = 'register')
            return render_template('register.html')
        else:
            flash("passwords do not match", "error")
            return render_template('register.html')
#third route for the uploading user details
@app.route('/upload_house', methods = ['POST', 'GET'])
def upload_page():
    if request.method == 'GET':
        return render_template('landlords.html')
    else:
        flash ("You have succeefully updated your new house into the system",'info')
        district = request.form['district']
        division = request.form['division']
        type_of_house = request.form['typeOfHouse']
        number_of_rooms = request.form['numberOfRooms']
        mrent = request.form['mrent']
        cman_name = request.form['cman_name']
        cman_phone = request.form['cman_phone']
        db.create_table_landlords()
        db.insert_landlords(district = district, division = division, typeofhouse=type_of_house, numofrooms=number_of_rooms,mrent=mrent, cman_name = cman_name, cman_phone = cman_phone, table_name = 'landlords')
        return render_template('landlords.html')
#last route for the registration
@app.route('/verify', methods = ['POST', 'GET'])
def Verify():
    return render_template('verify.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug= True)
