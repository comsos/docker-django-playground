from django.db import models

# Create your models here.
class Message(models.Model):

    message = models.TextField()
    send_to = models.CharField()
    secret_question = models.TextField()
    secret_answer = models.TextField()
    reply = models.TextField()
