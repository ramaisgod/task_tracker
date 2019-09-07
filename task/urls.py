from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('add_project', add_project, name='add_project'),   
    path('add_task', add_task, name='add_task'),
    path('add_activity', add_activity, name='add_activity'),    
    path('project_list', project_list, name='project_list'),
]
