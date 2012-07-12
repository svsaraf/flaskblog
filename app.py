"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/ber/')
def ber():
    """Render the website's about page."""
    return render_template('ber.html')

@app.route('/zdna/')
def zdna():
    """Render the website's about page."""
    return render_template('zdna.html')

@app.route('/myosin/')
def myosin():
    """Render the website's about page."""
    return render_template('myosin.html')
    
@app.route('/mems/')
def mems():
    """Render the website's about page."""
    return render_template('mems.html')
    
@app.route('/folding/')
def folding():
    """Render the website's about page."""
    return render_template('folding.html')
    
@app.route('/flu/')
def flu():
    """Render the website's about page."""
    return render_template('flu.html')
    
@app.route('/iphone/')
def iphone():
    """Render the website's about page."""
    return render_template('iphone.html')
    
@app.route('/memorybean/')
def memorybean():
    """Render the website's about page."""
    return render_template('memorybean.html')

@app.route('/research/')
def research():
    """Render the website's about page."""
    return render_template('research.html')

@app.route('/projects/')
def projects():
    """Render the website's about page."""
    return render_template('projects.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/static/<path:filename>')
def send_image(file_name):
    """Send images."""
    return app.send_static_file(app.config['static'], file_name, as_attachment=False)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=60'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
