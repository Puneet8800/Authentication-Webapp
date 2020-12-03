from django.conf import settings
from django.db import models
from encrypted_fields import fields
#https://pypi.org/project/django-searchable-encrypted-fields/

class UserDetail(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email = models.EmailField()
    dateOfBirth = models.DateField()
    fullName = models.CharField(max_length=200)
    ssn = fields.EncryptedIntegerField()

    def __str__(self):
        return self.fullName
