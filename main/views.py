from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245895',
        'name': 'Ridya Azizah Khayyira Mumtaz',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)