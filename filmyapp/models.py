from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} "


# class Movie(models.Model):
#     title = models.CharField(max_length=64)
#     year = models.IntegerField()
#     directory = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default=None)
#     category = models.ManyToManyField('Category')




class Film(models.Model):
    title = models.CharField(max_length=64)
    year = models.IntegerField()
    directory = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, related_name='directed_by')
    screen_play = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, related_name='screen_play_by', verbose_name='Scenarzysta')
    category = models.ManyToManyField('Category')
    Studio = models.ForeignKey('Studio', on_delete=models.CASCADE, null=True, related_name='produced_by', verbose_name='Studio')

    def __str__(self):
        return f"{self.title} {self.year}"

class Studio(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.city}"
