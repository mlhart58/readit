from	django.core.urlresolvers	import	reverse
from	django.db									import models
from	django.utils.timezone			import now

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
		return "{} by {}".format(self.title, self.list_authors())
		
	def list_authors (self):
		""" Function doc """
		return ", ".join([author.name for author in self.authors.all()])
	
	def save (self, *args, **kwargs):
		""" Function doc """
		if (self.review and self.date_reviewed is None):
			self.date_reviewed = now()
		super(Book, self).save(*args, **kwargs)
		"""
		You need to call this super class method to do the actual "save"
		You also need to call this "after" the work you want to save.
		if you have something to do after the super/save takes place, 
		add that code after the super/save call
		"""		
		

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
		
	def get_absolute_url (self):
		""" Function doc """
		return reverse(	'author-detail',
										kwargs={'pk': self.pk})
		
