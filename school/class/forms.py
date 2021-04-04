from .models import Student,Teacher,User
from django import forms

class Teacher_reg(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')
        widgets={
            'password':forms.PasswordInput(),
        }