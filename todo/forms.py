from django import forms

from .models import ToDoItem

from datetime import date

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['task_name', 'task_desc', 'due_date']

class EditTaskForm(forms.Form):
    task_name = forms.CharField(max_length = 200, required = True)
    task_desc = forms.CharField(max_length = 100, required = False)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required = False)