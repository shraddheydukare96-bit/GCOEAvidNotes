from django.shortcuts import render

# Create your views here.

def home(request):
    """
    This view renders the homepage (index.html).
    """
    return render(request, 'mainsite/index.html')

def notes_page(request):
    """
    This view renders the notes page (notes.html).
    """
    return render(request, 'mainsite/notes.html')

def videos_page(request):
    """
    This view renders the videos page (videos.html).
    """
    return render(request, 'mainsite/videos.html')

def pyqs_page(request):
    """
    This view renders the Previous Year Questions page (pyqs.html).
    """
    return render(request, 'mainsite/pyqs.html')

def about_page(request):
    """
    This view renders the about page (about.html).
    """
    return render(request, 'mainsite/about.html')

def search_page(request):
    """
    This view renders the search results page (search.html).
    """
    return render(request, 'mainsite/search.html')
