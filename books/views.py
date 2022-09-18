from django.shortcuts import render,redirect
from books import forms
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from books.models import Books

# Create your views here.

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})


    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{form:form})

class LoginView(View):

    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,'login.html',{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("login successful")
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})

        return render(request,'login.html')

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')

class BookAddView(View):

    def get(self,request,*args,**kwargs):
        form=forms.BookForm()
        return render(request,'add-book.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.BookForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('index')
        else:
            return render(request,'add-book.html',{"form":form})

class BookListView(View):
    def get(self,request,*args,**kwargs):
        all_books=Books.objects.filter(user=request.user)
        return render(request,'book-list.html',{"book":all_books})


class BookDetailView(View):

     def get(self,request,*args,**kwargs):
         id=kwargs.get("id")
         book=Books.objects.get(id=id)
         return render(request,'todo-detail.html',{"book":book})