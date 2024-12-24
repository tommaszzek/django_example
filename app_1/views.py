from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('dosik')
    return render(request,'app_1/dane.html')
    