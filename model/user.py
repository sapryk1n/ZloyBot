from peewee import *

from model.base_entity import BaseEntity


class User(BaseEntity):
    username = TextField()
    user_id = IntegerField(unique=True)
    
    class Meta:
        db_table = 'users'
