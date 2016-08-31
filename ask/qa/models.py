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
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User,related_name='author_question',)
    likes = models.ManyToManyField(User,related_name='likes_question')

class Answer(models.Model):                                                   
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question,related_name='question_answer')
    author = models.ForeignKey(User,related_name='author_question')
