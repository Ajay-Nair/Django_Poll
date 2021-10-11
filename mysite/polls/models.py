from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("Date published")

class Choice(models.Model):
    def __str__(self):
        return self.choise_text
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)