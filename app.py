from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)



# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'eduardo.er.ramirez@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'jqku emne ftsh tadk'  # Replace with your app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'eduardo.er.ramirez@gmail.com'  # Replace with your Gmail address

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message('New Contact Form Submission', recipients=['eduardo.er.ramirez@gmail.com'])  # Replace with your destination email
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



# app gmail psw 'jqku emne ftsh tadk'
# DELETE THIS PY FILE IF NOT IN USE, THIS IS FOR THE FLASK APP, CODE BEING USE IN THE 
# CARWASH1.QMD FILE
# python app.py
# the above line is to be ran for the app to be live in my local server and be able to send emails at a local level.
