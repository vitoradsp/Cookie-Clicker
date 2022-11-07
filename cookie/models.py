from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userinfo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    ac = models.IntegerField()
    def __str__(self):
        return self.usuario.username