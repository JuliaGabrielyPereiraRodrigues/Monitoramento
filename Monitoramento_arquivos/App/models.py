from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
