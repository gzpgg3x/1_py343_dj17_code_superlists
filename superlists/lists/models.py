from django.db import models

class Item(models.Model):
    # text = model.TextField()
    text = models.TextField(default='')
