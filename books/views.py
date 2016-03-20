# from	django.http				import	HttpResponse
from	django.contrib.auth.decorators	import	login_required
from	django.core.urlresolvers				import	reverse
from	django.db.models								import	Count
from	django.shortcuts								import	(	redirect,
																								render, 
																								get_object_or_404
																							)
from	django.views.generic						import	DetailView, View
from	django.views.generic.edit				import	CreateView

from	.forms	import	ReviewForm, BookForm
from	.models	import	Author, Book

# Create your views here.
def list_books (request):
	"""
	List the books that have reviews
	"""
	
	books 	= Book.objects.exclude(date_reviewed__isnull=True)\
												.prefetch_related('authors')
	context	=	{
		'books': books,
	}
	# Saving the below "return" as an insteresting example"
	#return HttpResponse(request.user.username)
	return render(request, "list.html", context)
	

class AuthorList(View):
	def get(self, request):
		authors = Author.objects.annotate(
			published_books=Count('books')
		).filter(
			published_books__gt=0
		)
		context = {
			'authors': authors,
		}
		return render(request, "authors.html", context)
		

class BookDetail(DetailView):
	model = Book
	template_name = "book.html"
	
	
class AuthorDetail(DetailView):
	model = Author
	template_name = "author.html"

	
class ReviewList(View):
	"""
	List all of the books that we want to review.
	"""
	def get(self, request):
		books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
		
		context = {
			'books':	books,
			'form':		BookForm,
		}
		return render(request, "list-to-review.html", context)
	#End - def get(self, request):
	
	def post(self, request):
		form = BookForm(request.POST)
		books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
		
		if form.is_valid():
			form.save()
			return redirect('review-books')
			
		context = {
			'form':		form,
			'books':	books,
		}
		return render(request, "list-to-review.html", context)			
	#End - def post(self, request):


@login_required
def review_book(request, pk):
	"""
	Review an individual book
	"""
	book = get_object_or_404(Book, pk=pk)
	
	if request.method == 'POST':
		# Process our form
		form = ReviewForm(request.POST)
		
		if form.is_valid():
			# If Boolean is not required (i.e. you mark it true)
			# then is will not be in 'cleaned_data'
			# book.is_favourite = form.cleaned_data['is_favourite']
			book.review				= form.cleaned_data['review']
			book.reviewed_by	= request.user
			book.save()
			
			return redirect('review-books')
		#End - if form.is_valid():
	else:
		form = ReviewForm
	#End - if request.method == 'POST':
	
	context = {
		'book': book,
		'form': form,
	}
	
	return render(request, "review-book.html", context)
	
	
class CreateAuthor(CreateView):
	""" Class doc """
	model					=	Author
	fields				=	['name',]
	template_name	=	"create-author.html"

	def get_success_url(self):
		return	reverse('review-books')
