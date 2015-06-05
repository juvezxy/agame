from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text

class Segment(models.Model):
    question = models.ForeignKey(Question)
    segment_text = models.CharField(max_length=200)
    index = models.IntegerField(default=0)
    def __unicode__(self):
        return self.segment_text