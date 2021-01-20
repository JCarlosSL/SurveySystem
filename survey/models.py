from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)

    def questions(self):
        return Question.objects.filter(survey=self.pk)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)

class Response(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    response_text = models.TextField()

class BaseResponse(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    #response = models.ForeignKey(Response,on_delete=models.CASCADE)
    response_text = models.TextField()



    