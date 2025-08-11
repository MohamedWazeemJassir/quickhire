from django import forms
from .models import Job

class Form(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'salary', 'expiry_date', 'apply_link', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }