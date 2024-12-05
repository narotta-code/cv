from django.shortcuts import render

# Create your views here.
def accountHome(request):
    return render (request, 'courier/account_home.html')
