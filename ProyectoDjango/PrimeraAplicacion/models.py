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
    


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField(max_length=200)
    biography = models.TextField(max_length=500)

    def __str__(self):
        return self.website

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_data = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")


    def __str__(self):
        return self.title
    
