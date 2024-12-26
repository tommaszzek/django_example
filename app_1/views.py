from django.shortcuts import render
from django.http import Http404,HttpResponse


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

def list (request):
    return HttpResponse('Lista pytan')

def answers(request,question_id):
    return HttpResponse(f'Odpowiedziales na pytanie  {question_id}')

def results(request,question_id):
    return HttpResponse(f'Wynik z p {question_id}')

def question(request,question_id):
    return HttpResponse(f'Pytanie  {question_id}')
    