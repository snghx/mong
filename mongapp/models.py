from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import Users


# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, verbose_name="현유저")
    pub_date = models.DateField(auto_now_add=True)
    cal = models.CharField(max_length=1000)
    WALK_CHOICES = (
        ('0', '0보 이상'),
        ('1000', '1000보 이상'),
        ('2000', '2000보 이상'),
        ('3000', '3000보 이상'),
        ('4000', '4000보 이상'),
        ('5000', '5000보 이상'),
        ('6000', '6000보 이상'),
        ('7000', '7000보 이상'),
        ('8000', '8000보 이상'),
        ('9000', '9000보 이상'),
        ('10000', '10000보 이상'),
    )
    walk = models.CharField(max_length=10000, null=True, choices=WALK_CHOICES, verbose_name='walk')
    hour = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pub_date

class Mongs(models.Model):
    monguser = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, verbose_name="현유저")
