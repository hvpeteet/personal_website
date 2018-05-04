import jinja2
import os
import webapp2
import logging
import datetime
from google.appengine.api import users
from google.appengine.ext import ndb

import urllib2

LOADER = jinja2.FileSystemLoader(os.path.dirname(__file__))
jinja_environment = jinja2.Environment(loader = LOADER)

class BioHandler(webapp2.RequestHandler):    
    def get(self): 
        template_values = {}
        template = jinja_environment.get_template('templates/bio2.html')
        self.response.out.write(template.render(template_values))

class ProjectsHandler(webapp2.RequestHandler):    
    def get(self): 
        template_values = {}
        template = jinja_environment.get_template('templates/projects.html')
        self.response.out.write(template.render(template_values))


routes = [
    ('/projects', ProjectsHandler),
    ('/.*', BioHandler), 
]
app = webapp2.WSGIApplication(routes, debug=True)