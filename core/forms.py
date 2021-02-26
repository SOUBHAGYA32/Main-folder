from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from .models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name','emp_code','mobile','email', 'desig')
        labels = {
            'name':'Full Name',
            'emp_code':'Employee Code',
            'mobile':'Mobile Number',
            'email':'Email',
            'desig':'Employee Designation'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['desig'].empty_label = "Select"
        self.fields['emp_code'].required = False