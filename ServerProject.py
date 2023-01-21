from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = 'SITE_KEY'
app.config['RECAPTCHA_SECRET_KEY'] = 'SECRET_KEY'
recaptcha = ReCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)


@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        if recaptcha.verify():
            data = request.form.to_dict()
            return redirect('/#contact_submitted')
        else:
            return redirect('/#contact_error')
    else:
        print('Something went wrong. PLease try again')
        return redirect('#contact_error')
