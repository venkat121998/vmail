from django import forms

from .models import vmailuser,Vmails

class CreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = vmailuser
        fields = ('mail_id', 'user_name','password')

class LoginForm(forms.Form):
    vmail = forms.CharField(label='Vmail', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class ComposeForm(forms.ModelForm):
    to = forms.CharField()
    class Meta:
        model = Vmails
        fields = ('to','title', 'body')