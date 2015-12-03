# -*- coding: utf-8 -*- 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from model import ViewCounter

BASE_PATH = os.path.dirname(__file__)

def increment_count():
    for counter in ViewCounter.query():
        counter.count = counter.count+1
        counter.put()
        return
    counter = ViewCounter(count = 1)
    counter.put()
    return

class About(webapp.RequestHandler):
    def get(self, *args):
        increment_count()
        path = os.path.join(BASE_PATH, 'templates/index.html')
#         path = os.path.join(BASE_PATH, 'templates/chat.html')
        self.response.out.write(template.render(path, []))
class ViewInfo(webapp.RequestHandler):
    def get(self):
        path =  os.path.join(BASE_PATH, 'templates/view_info.html')
        self.response.out.write(template.render(path, {}))
class Structure(webapp.RequestHandler):
    def get(self, *args):
        path =  os.path.join(BASE_PATH, 'templates/structure.html')
        self.response.out.write(template.render(path, {}))
class MarkTest(webapp.RequestHandler):
    def get(self, *args):
        filePath =  'templates/mark_test.html'
        if self.request.get('t') == "c":
            filePath = 'templates/condition_test.html'
        elif self.request.get('t') == "m":
            filePath = 'templates/mark_test.html'
        self.response.out.write(template.render(os.path.join(BASE_PATH, filePath), {}))
application = webapp.WSGIApplication([
                                      ('/', About),
                                      ('/ViewInfo', ViewInfo),
                                      ('/structure', Structure),
                                      ('/test', MarkTest),
                                    ], debug=True)
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()
