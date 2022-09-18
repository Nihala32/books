from django import forms
from django.contrib.auth.models import User
from books.models import Books
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))



class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["book_name"]
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-controls"}),
        }

