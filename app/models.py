from django.db import models


# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.name