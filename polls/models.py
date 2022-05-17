from django.utils import timezone
from django.db import models
import datetime


class Question(models.Model):
    def __str__(self): return self.question_text + ":" + self.pub_date.strftime('%m/%d/%Y')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
    def __str__(self): return self.choice_text + ":" + self.votes.__str__()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
