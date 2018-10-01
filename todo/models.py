from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    note_title = models.CharField(max_length=50)
    note_text = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title
