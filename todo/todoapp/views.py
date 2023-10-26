from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm, TodoEditForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

def home(request):
    # Calculate the start and end dates for this week
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    todos_this_week = Todo.objects.filter(due_date__gte=today, due_date__lt=next_week)

    return render(request, 'todo/home.html', {
        'todos_this_week': todos_this_week,
    })

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# def todo_detail(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'POST':
        edit_form = TodoEditForm(request.POST, instance=todo)
        if edit_form.is_valid():
            edit_form.save()
            # Redirect to the to-do detail page after editing
            return redirect('todo:todo_list')
    else:
        edit_form = TodoEditForm(instance=todo)

    return render(request, 'todo/todo_edit.html', {'todo': todo, 'edit_form': edit_form})

def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

@login_required
def my_protected_view(request):
    return render(request, 'home.html')