from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, related_name='admin_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='group_memberships', blank=True)

    def __str__(self):
        return self.name