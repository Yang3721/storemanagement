from django import forms
from django.template import RequestContext
#from .models import User


class UserForm(forms.Form):
    #    model = User
    #class Meta:
    #    model = User
    #   fields = ('Title', 'lgoin')
        username = forms.CharField(label='username')
        password = forms.CharField(label='password')


class SearchForm(forms.Form):
    keyword = forms.CharField(label='keyword')


class BorrowForm(forms.Form):
    borrow_message = forms.CharField(label='borrow_message')