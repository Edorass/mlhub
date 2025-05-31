from django import forms
from .models import MLproject

class MLProjectForm(forms.ModelForm):
    class Meta:
        model = MLproject
        fields = ['title', 'description', 'tech_stack', 'github_link', 'image']
