from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=128)
    pub_date = models.DateTimeField(verbose_name='Date Published')
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.choice_text + " with " + self.votes +" votes!"