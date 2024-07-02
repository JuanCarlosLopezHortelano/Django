from django.db import models

# Create your models here.
class Carro(models.Model):
    title = models.TextField(max_length=255)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_data = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title