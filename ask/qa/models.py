from dgango.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
    def new() : pass                                                            
    def popular() : pass 

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.CharField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User)
    likes = models.CharField(max_length=255)

class Answer(models.Model):                                                   
    text = models.CharField()  
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
