from	django.http				import	HttpResponse
from	django.shortcuts	import	render

# Create your views here.
def list_books (request):
	""" Function doc """
	return HttpResponse(request.user.username)
	
