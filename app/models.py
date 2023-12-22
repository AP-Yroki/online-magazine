from django.db import models

# Create your models here.


class Estimation(models.Model):
    number = models.CharField(max_length=20, verbose_name='Число')

class Subject(models.Model):
    naming = models.CharField(max_length=20, verbose_name='Наименование предмета')


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    school_object = models.CharField(max_length=20, verbose_name='Предмет')
    evaluation = models.CharField(max_length=20, verbose_name='Оценка')
    average_score = models.CharField(max_length=20, verbose_name='Средний балл')
    estimation = models.ForeignKey(Estimation, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)