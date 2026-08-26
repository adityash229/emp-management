from django.contrib import admin
from django.urls import path, include  
from .router import router
from Empdetails.views import employees_list

from Empdetails.views import(
    EmpCreatedetails,
    EmpGetdetails,
    EmpUpdatedetails,
    EmpDeletedetails,
)

urlpatterns = [
    
    path(
        'api/post/emp-details/',
        EmpCreatedetails.as_view()
    ),

    path(
        'api/get/emp-details/',
        EmpGetdetails.as_view()
    ),

    
    

    path(
        'api/put/emp-details/<int:pk>/',
        EmpUpdatedetails.as_view()
    ),

    path(
        'api/delete/emp-details/<int:pk>/',
        EmpDeletedetails.as_view()
    ),
]
