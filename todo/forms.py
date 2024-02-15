from django import forms

from .models import Todo

class TodoCreateForm(forms.ModelForm):
  class Meta:
    model = Todo
    exclude = ['date']
    labels = {
      'text': 'Title',
      'status': 'Status'
    }