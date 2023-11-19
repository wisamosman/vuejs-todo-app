from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    notes = models.TextField(max_length=400)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title