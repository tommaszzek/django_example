from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("<int:question_id>/",views.question,name='question'),
    path("<int:question_id>/answer",views.answers,name='answer'),
    path("<int:question_id>/results",views.results,name='results'),
]
app_name='app_1'