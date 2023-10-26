from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home'), 
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='create_todo'),
    path('<int:pk>/update/', views.todo_update, name='update_todo'),
    path('<int:pk>/delete/', views.todo_delete, name='delete_todo'),
    path('<int:todo_id>/edit/', views.todo_edit, name='todo_edit'),

]
