from flask import render_template

def hello_world():
    return "Hello, MVC框架......"

def index():
    return render_template('index.html') 

def projects():
    return render_template('projects.html')

def resume():
    return render_template('resume.html')

def contact():
    return render_template('contact.html')

def otherpictures():
    return render_template('otherpictures.html')

def notebook():
    return render_template('notebook.html')

def feedback():
    return render_template('feedback.html')

def myproject():
    return render_template('myproject.html')

def googlepatent():
    return render_template('googlepatent.html')

def ppgpro():
    return render_template('ppgpro.html')