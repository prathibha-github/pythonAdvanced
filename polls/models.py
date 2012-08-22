from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
AUDIENCE_CHOICES = [
                    ('corp','Corporate Users'),
                    ('pub', 'Public Users'),]

class Poll(models.Model):
    question = models.CharField(max_length=128)
    pub_date = models.DateTimeField(verbose_name='Date Published',auto_now_add=True)
    audience = models.CharField(max_length=32, choices=AUDIENCE_CHOICES)
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.choice_text