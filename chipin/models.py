from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_groups')
    members = models.ManyToManyField(User, related_name='group_memberships', blank=True)
    invited_users = models.ManyToManyField(User, related_name='pending_invitations', blank=True)

class GroupJoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='join_requests')
    is_approved = models.BooleanField(default=False)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)  # Tracks users who voted
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted the comment
    group = models.ForeignKey(Group, related_name='comments', on_delete=models.CASCADE)  # Group associated with the comment
    content = models.TextField()  # The comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was posted
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the latest update

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."  # Show only first 20 chars for preview
    

# model from week 6, idk if it goes in users or chipin

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    total_spend = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')  # Can be 'Pending' or 'Active'
    group = models.ForeignKey(Group, related_name='events', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='event_memberships', blank=True)  

    def calculate_share(self):
        members_count = self.group.members.count()
        if members_count == 0:
            return 0
        return self.total_spend / members_count

    def check_status(self):
        """ Check if all members' max spend can cover the event. """
        share = self.calculate_share()
        for member in self.group.members.all():
            if member.profile.max_spend < share:
                self.status = 'Pending'
                return False
        self.status = 'Active'
        return True