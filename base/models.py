from django.db import models
from django.contrib.auth.models import User


class DevGrades(models.Model):  # Джуниор, Миддл, Сеньор, Стажер
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    employer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Работодатель
    devgrade = models.ForeignKey(DevGrades, on_delete=models.SET_NULL, null=True)  # Уровень
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)  # Изменено
    created = models.DateTimeField(auto_now_add=True)  # Добавлено, эти можно использовать при сортировке
 

    class Meta: 
        ordering = ['-created']  # Наверное можно вывести прямо отсюда фильтр по Джунам, Сеньорам и тд
        # Но вот это ordering поменять нельзя, как и verbose_name, чекните \ITwebsite\ITwebsite\доп Инфа.txt


    def __str__(self):
        return self.name
    
  # Здесь надо делать опросник
class Quiz(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    
    def __str__(self):
        return self.offer.name
        