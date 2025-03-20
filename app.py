from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # Change if your MySQL server is on a different host
app.config['MYSQL_USER'] = 'your_username'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'flask_registration'

mysql = MySQL(app)

app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        dob = request.form['dob']
        gender = request.form['gender']

        # Insert user data into the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (fullname, email, password, phone, dob, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                    (fullname, email, password, phone, dob, gender))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)