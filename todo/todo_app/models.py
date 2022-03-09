from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    a = (
        ("yangi","yangi"),
        ('bajarildi','bajarildi')
    )
    nom = models.CharField(max_length=50)
    batafsil = models.CharField(max_length=120)
    status = models.CharField(max_length=30,choices=a)
    vaqt = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}({self.batafsil},{self.vaqt},{self.status})"
