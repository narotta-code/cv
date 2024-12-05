from django.shortcuts import render

# Create your views here.
def cargo_View(request):
    return render(request, 'courier/cargo.html')