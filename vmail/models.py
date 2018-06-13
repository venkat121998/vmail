from django.db import models
from datetime import datetime
# Create your models here.
class vmailuser(models.Model):
    mail_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    last_login = models.DateTimeField(default=datetime.now,blank=True)
    login = models.IntegerField(default=0)
    #1=logged in
    #0=logged out
    def __str__(self):
        return self.mail_id
    class Meta:
        verbose_name_plural="vmailusers"

class Vmails(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    sent_at = models.DateTimeField(default=datetime.now,blank=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    visit = models.IntegerField(default=0)
