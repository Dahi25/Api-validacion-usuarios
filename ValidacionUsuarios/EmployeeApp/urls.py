from django.urls import re_path  as url
from EmployeeApp import views


urlpatterns = [
    url(r'^nombre$',views.nombreApi),
     url(r'^nombre/',views.nombreApi),
  
]