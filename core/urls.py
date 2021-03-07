from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.addemp, name='addemp'),
    path('dash/',views.dash,name='dash'), # get req. to retrieve and display all records
]