# -*- coding: utf-8 -*- 
from google.appengine.ext import ndb
from datetime import datetime
from google.appengine.ext.endpoints import InternalServerErrorException

class ViewCounter(ndb.Model):
    count = ndb.IntegerProperty(default=0)
class Message(ndb.Model):
    content= ndb.StringProperty(required = True)
    date = ndb.StringProperty(required = True)
    def _pre_put_hook(self):
        len_after_encode = len(self.content.encode('utf-8'))
        if len_after_encode==0 or len_after_encode > 1400:
            raise InternalServerErrorException
        self.date = datetime.now().strftime('%Y%m%d%H%M%S')