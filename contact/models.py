from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()


    def __str__(self):
        return self.name
