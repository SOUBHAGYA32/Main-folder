from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.addemp, name='addemp'),
    path('<int:id>/addemp/', views.addemp, name='employee_update'),,
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('dash/',views.dash,name='dash') # get req. to retrieve and display all records
]