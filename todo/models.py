from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoItem(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.TextField(verbose_name="Task description", max_length=1000, blank=True)
    date_added = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_added']
    
    def __str__(self):
        if self.task_desc:
            return f"{self.task_name} - {self.task_desc}"
        else:
            return self.task_name