from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('view_todo',views.view_todo,name='view_todo'),
    path('update_todo/<int:id>/',views.update_todo,name='update_todo'),
    path('del_todo/<int:id>/',views.del_todo,name='del_todo')
]