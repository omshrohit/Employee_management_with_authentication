from django.contrib import admin
from django.urls import path
from . views import home,view_all_enployee,add_employee,remove_employee,filter_employee,update_details

urlpatterns = [
    path("",home,name='home'),
    path("home",home,name='home'),
    path('view_emp',view_all_enployee,name='view_emp'),
    path('add_emp',add_employee,name='add_emp'),
    path("remove_emp",remove_employee,name='remove_emp'),
    path('remove_emp/<int:emp_id>',remove_employee,name='remove_emp'),
    path('filter_emp',filter_employee,name='filter_enp'),
    path('update_details',update_details,name="update_details"),
    path('update_details/<id>',update_details,name="update_details")
]

