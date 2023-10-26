from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed', 'due_date', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }


class TodoEditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'due_date', 'description']