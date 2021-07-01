from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    submission_id = models.IntegerField(null=True)

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)
# Create your models here.
