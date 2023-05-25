from django.db import models

#Define uma classe chamada "Task" que é um modelo no contexto de um aplicativo Django
class Task(models.Model):
  title=models.CharField(max_length=50)
  description=models.TextField()
  due_date=models.DateField()

#Define uma classe chamada "Musician" que é um modelo no contexto de um aplicativo Django
class Musician(models.Model):
  nome = models.CharField(max_length=50)
  sobrenome = models.CharField(max_length=50)
  instrumento = models.CharField(max_length=100)
