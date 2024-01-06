import mongoengine as me

class User(me.Document):
    name = me.StringField(required=True)
    age = me.IntField(required=True)