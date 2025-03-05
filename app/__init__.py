from flask import Flask
from app.route import hello_world, index,projects,resume,contact,otherpictures,feedback,notebook,myproject,googlepatent,ppgpro

def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index.html', 'index', index)
    app.add_url_rule('/projects.html', 'projects', projects)
    app.add_url_rule('/resume.html', 'resume', resume)
    app.add_url_rule('/contact.html', 'contact', contact)
    app.add_url_rule('/otherpictures.html', 'otherpictures', otherpictures)
    app.add_url_rule('/feedback.html', 'feedback', feedback)
    app.add_url_rule('/notebook.html', 'notebook', notebook)
    app.add_url_rule('/myproject.html', 'myproject', myproject)
    app.add_url_rule('/googlepatent.html', 'googlepatent', googlepatent)
    app.add_url_rule('/ppgpro.html', 'ppgpro', ppgpro)
    app.add_url_rule('/special.html', 'special', special)
    return app
