from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=200)
	book = models.ForeignKey(Book, related_name='author', on_delete=models.CASCADE)

	def __str__(self):
		return self.name
				