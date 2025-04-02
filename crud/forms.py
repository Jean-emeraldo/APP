from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['outcome', 'created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'glucose': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_pressure': forms.NumberInput(attrs={'class': 'form-control'}),
        }