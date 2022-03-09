from django.contrib import admin
from django.urls import path
from todo_app.views import all_todo, remove, regview, logview, LogOut, todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', all_todo, name='todo'),
    path('todo/submit', todo, name='submit'),
    path('del/<int:son>', remove, name='del'),
    path('reg/', regview, name='reg'),
    path('', logview, name='login'),
    path('logout/', LogOut, name='logout'),



]
