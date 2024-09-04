from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
            'npm' : '2306256362',
            'name': 'Isaac Jesse Boentoro',
            'class': 'PBD KKI'
    }
    return render(request, "main.html", context)
