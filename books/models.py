from django.db import models

# Create your models here.

class Book(models.Model):
	""" Class doc """
	title	= models.CharField(max_length=150)
	authors	=	models.ManyToManyField("Author", related_name="books")
	review	=	models.TextField(blank=True, null=True)
	date_reviewed	=	models.DateTimeField(blank=True, null=True)
	is_favourite	= models.BooleanField(
		default=False,
		verbose_name="Favourite?"
	)
	
	def __str__ (self):
		""" Function doc """
		return self.title
		

class Author(models.Model):
	""" Class doc """
	name	= models.CharField(
		max_length=70,
		help_text="Use pen name, not real name",
		unique=True
	)
	
	def __str__ (self):
		""" Function doc """
		return self.name
		
	
