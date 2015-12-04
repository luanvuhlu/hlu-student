# -*- coding: utf-8 -*- 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, cgi, HTMLParser
from google.appengine.ext.webapp import template
from model import ViewCounter, Message

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
#         path = os.path.join(BASE_PATH, 'templates/index.html')
        path = os.path.join(BASE_PATH, 'templates/chat.html')
        template_values = {
                           'messages':  Message.query().order(-Message.date)
                           }
        self.response.out.write(template.render(path, template_values ))
class UpdateMessage(webapp.RequestHandler):
    def get(self, *args):
        content = self.request.get("content")
        content = cgi.escape(content);
        len_after_encode = len(content.encode('utf-8'))
        if len_after_encode == 0 or len_after_encode > 1400:
            self.response.out.write('')
            return
        message = Message(content = content)
        message.put()
        self.response.out.write(message.color)
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
                                      ('/add-message', UpdateMessage),
                                    ], debug=True)
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()
