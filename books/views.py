# from	django.http				import	HttpResponse
from	django.shortcuts	import	render

from	.models	import Book

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
	
