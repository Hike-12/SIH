from django.db import models

# Create your models here.
class Quiz(models.Model):
    number = models.IntegerField(default=0)
    question = models.CharField(max_length=200, default = "None")
    option_1 = models.CharField(max_length=50, default = "None")
    option_2 = models.CharField(max_length=50, default = "None")
    option_3 = models.CharField(max_length=50, default = "None")
    option_4 = models.CharField(max_length=50, default = "None")
    answer = models.CharField(max_length=50, default="None")
    status = models.BooleanField(default=False)
    desc = models.TextField(default="None")
    
    def __str__(self):
        return self.question
    
class Hero_Day(models.Model):
    date = models.DateField()
    event = models.CharField(max_length=200, default = "None")
    person = models.CharField(max_length=200, default = "None")
    event_desc = models.TextField(default="None")
    person_desc = models.TextField(default="None")
    
    def __str__(self):
        return self.event
    
    
class Short(models.Model):
    tag = models.CharField(max_length=200, default = "None")
    section = models.TextField(default="None")
    description = models.TextField(default="None")
    
    def __str__(self):
        return self.section
    