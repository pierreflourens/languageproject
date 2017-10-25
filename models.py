from google.appengine.ext import ndb

#to create a database


class PierreWord(ndb.Model):
    english = ndb.StringProperty()
    french = ndb.StringProperty()
    spanish = ndb.StringProperty()
