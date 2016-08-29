from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
    def new() :
        pass                                                            
    def popular() :  
        pass 

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User,related_name='author_set')
    likes = models.ManyToManyField(User,related_name='likes_set')

class Answer(models.Model):                                                   
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
