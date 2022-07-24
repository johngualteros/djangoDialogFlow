from django.shortcuts import render

# Create your views here.
def requests(request):
    return render(request,'requests.html')
