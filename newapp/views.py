from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to Django Templates!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'home.html', context)
