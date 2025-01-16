from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'yourUsername',
            'type':'text',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'yourEmail',
            'type':'email',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'yourPassword',
            'type':'password',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'yourPassword',
            'type':'password',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6',
        })
        

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
