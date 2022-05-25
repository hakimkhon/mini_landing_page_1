from django.db import models

class Url(models.Model):
    url = models.URLField(help_text='Iltimos to\'g\ri URL kiriting!')  # Varchar()
    creted_at = models.DateTimeField(auto_now_add = True)   # TIMESTAMP
    modified_at = models.DateTimeField(auto_now = True)

