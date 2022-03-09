from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Todo

def all_todo(request):
    if request.user.is_authenticated:
        t = Todo.objects.filter(user=request.user)
        return render(request, 'todo.html', {"todo": t})
    else:
        return redirect('login')

def remove(request, son):
    if request.user.is_authenticated:
        h = Todo.objects.get(id=son)
        h.delete()
        return redirect('/todo')
    else:
        return redirect('/todo')

def todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Todo.objects.create(
                nom=request.POST.get('n'),
                batafsil=request.POST.get('b'),
                status=request.POST.get('s'),
                vaqt=request.POST.get('v'),
                user=request.user
            )
            return redirect('todo')
        else:
            return redirect('login')
def regview(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['parol']
        )
        login(request, user)
        return redirect("todo")
    return render(request, "reg.html")

def logview(request):
    if request.method == 'POST':
        l = request.POST.get('login')
        p = request.POST.get('parol')
        users = authenticate(request, username=l, password=p)
        if users is None:
            return redirect('/')
        else:
            login(request, users)
            return redirect('/todo')
    return render(request, 'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')