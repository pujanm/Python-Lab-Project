from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, TeacherProfile
import re

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='SAP ID')

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None


class UserProfileForm(forms.ModelForm):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    semester = forms.IntegerField()
    class Meta():
        model = UserProfile
        fields = ('fname', 'lname', 'semester', 'phone_no', 'batch')


class TeacherProfileForm(forms.ModelForm):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')

    class Meta():
        model = TeacherProfile
        fields = ('fname', 'lname')
