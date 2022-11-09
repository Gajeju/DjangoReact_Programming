from django.db import models

class Post(models.Model):
    messate = models.TextField()
    created_ta = models.DateTimeField(auto_now_add=True)
    updated_ta = models.DateTimeField(auto_now=True)
