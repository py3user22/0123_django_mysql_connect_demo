from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home123_mysql_demo1.html', {})


