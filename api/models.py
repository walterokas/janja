from django.db import models

# Create your models here.
class JanjaSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=12)
    session_id = models.CharField(max_length=32)