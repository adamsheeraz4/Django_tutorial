
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

#one database that stores Questions
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # makes the ouput of .objects.all() readable
    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

#a diff database that stores choices
class Choice(models.Model):
    # each variable reps a database field in the model
    #links quesiton table to choice
    # the variable is a column name, when intialize a Choice object, I'll be adding rows to each column.
    # capitlization of variable makes a difference!
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

