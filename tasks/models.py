from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    
    content = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.content
