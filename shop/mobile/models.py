from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mobile(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    photo=models.ImageField(upload_to='mobile/')
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name

    class Meta:
        ordering=('name',)
