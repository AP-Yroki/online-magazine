from django import forms
from .models import Student, Estimation, Subject



class EstimationForm(forms.ModelForm):
    class Meta:
        model = Estimation
        fields = ['number']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['naming']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'