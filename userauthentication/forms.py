from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['data-toggle'] = 'tooltip'
        self.fields['password1'].widget.attrs['data-placement'] = 'right'
        self.fields['password1'].widget.attrs['title'] = 'Password Must be minimum of 8 Charcters. Password must not be related to above Information. Password shall contain Uppercase LowerCase Digits. Password shall contain Special Character @/+/-/_'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    USERTYPES = {
        ("1","Patient"),
        ("2","Doctor"),
    }
    userType = forms.ChoiceField(choices=USERTYPES, label="User Type", widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'userType']