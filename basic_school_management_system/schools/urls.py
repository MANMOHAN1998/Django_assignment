from django.urls import path
from .views import *

urlpatterns = [
    path('register-school/', registerschool.as_view(), name='registerschool'),
    path('add-student/', AddStudent.as_view(), name='addstudent'),
    path('update-student/', UpdateStudent.as_view(), name='Updatestudent'),

]
