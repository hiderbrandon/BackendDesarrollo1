from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Obra(models.Model):
    name = models.CharField(max_length=100)
    director = models.TextField()
    completed = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')

    def __str__(self):
        return self.name