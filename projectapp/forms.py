from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationsForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description']