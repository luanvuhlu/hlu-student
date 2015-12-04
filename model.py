# -*- coding: utf-8 -*- 
from google.appengine.ext import ndb
from datetime import datetime
import random

RANDOM_COLORS =['red', 'green', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 'light-blue', 'cyan', 'teal', 'green', 'light-green', 'lime']

class ViewCounter(ndb.Model):
    count = ndb.IntegerProperty(default=0)
class Message(ndb.Model):
    content = ndb.StringProperty(required = True, indexed = False)
    color = ndb.StringProperty(required = False, indexed = False)
    date = ndb.StringProperty(required = True)
    def _pre_put_hook(self):
        self.color = random.choice(RANDOM_COLORS)+'-color'
        self.date = datetime.now().strftime('%Y%m%d%H%M%S')