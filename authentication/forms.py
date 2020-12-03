from django import forms
from .models import UserDetail

class DateInput(forms.DateInput):
    input_type = 'date'

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = "__all__"
        exclude = ('user',)

        widgets = {
            'dateOfBirth': DateInput(),
        }

        labels = {
        	'email': 'Email',
        	'fullName': 'Full Name',
        	'dateOfBirth': 'Date Of Birth',
        	'ssn': 'Social Security Number'
        }
