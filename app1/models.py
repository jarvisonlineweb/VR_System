from django.db import models

# Create your models here.
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

class Room_Type(models.Model):
    TYPE_CHOICES = (
        ('S', 'Single'),
        ('D', 'Double'),
    )
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    Building = models.ForeignKey(Building, on_delete=models.CASCADE, default=1)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    Number = models.PositiveSmallIntegerField(default=0)
    Room_Type = models.ForeignKey(Room_Type, on_delete=models.CASCADE, default=1)
    Price = models.FloatField()

class BlockedDay(models.Model):
    id = models.AutoField(primary_key=True)
    Day = models.DateField()
    Room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)

