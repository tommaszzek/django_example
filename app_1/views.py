from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('dosik')
    question={
        'text':'Co znaczy skrót JS ?',
        'answers':[{'text':'Zrob swoje','correct':False },
                   {'text':'Zrob swoje','correct':False  },
                   {'text':'Java Script','correct':True },
                   {'text':'Zrob swoje' ,'correct':False }
                   ]
    }
  
    return render(request,'home.html',{'question':question})
    