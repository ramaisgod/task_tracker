from django import forms
from django.forms import ModelForm
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'true'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'true'

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'true'

