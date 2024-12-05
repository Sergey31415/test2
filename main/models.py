from django.db import models

class Prepod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    prepod = models.ForeignKey(Prepod, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)

