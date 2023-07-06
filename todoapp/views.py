from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import TodoForm
from todoapp.models import todoapp


def todo(request):
    return render(request,'index.html')

def addtodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('todo')
    return render(request,"addtodo.html",{'form':form})

def view_todo(request):
    data = todoapp.objects.all()
    return render(request,'view_todo.html',{'data':data})

def update_todo(request,id):
    data=todoapp.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_todo')
    return render(request,'update_todo.html',{'form':form})

def del_todo(request,id):
    todoapp.objects.get(id=id).delete()
    return redirect('view_todo')
