from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'), 
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='create_todo'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('<int:pk>/update/', views.todo_update, name='update_todo'),
    path('<int:pk>/delete/', views.todo_delete, name='delete_todo'),
]
