from django.db import models
from django.utils import timezone
from twitteruser.models import Twitter_user

class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    tweet_author = models.ForeignKey(Twitter_user, on_delete=models.CASCADE, related_name='filed_by')

