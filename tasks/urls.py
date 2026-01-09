from django.urls import path
from . import views

urlpatterns = [
    path('projects/<int:project_id>/tasks/create/',views.create_task,name='create_task' ),
    path('tasks/<int:task_id>/status/',views.update_task_status,name='update_task_status' ),
    path( 'tasks/<int:task_id>/',views.task_detail, name='task_detail'),

]
