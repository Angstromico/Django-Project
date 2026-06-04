from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField(auto_now=True)
    time = models.TimeField()
    guests = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.time}"