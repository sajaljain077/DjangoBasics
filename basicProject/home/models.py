from django.db import models




class Color(models.Model):
    color_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.color_name
    
class Person(models.Model):
    color = models.ForeignKey(Color, null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    address = models.CharField(max_length = 100, default=None, null =True)