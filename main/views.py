from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406404705',
        'name': 'Muhammad Fahri Muharram',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
