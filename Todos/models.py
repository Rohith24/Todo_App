from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class TodoList(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    def __unicode__(self):
        return self.name

class TodoItem(models.Model):
    item_id=models.ForeignKey(TodoList)
    description=models.CharField(max_length=255)
    duedate=models.DateField()
    status=models.BooleanField(default=False)

    def __unicode__(self):
        return self.item_id