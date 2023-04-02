from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
# Create your views here.


def register_request(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("in if condition")
            user = form.save()
            # login(request, user)  # skip
            return redirect("register")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="login.html", context={"login_form":form})




def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # admin
            password = form.cleaned_data.get('password') # admin
            user = authenticate(username=username, password=password) # returns user object
            print(user, user.__dict__)
            if user:
                login(request, user) # database save
                return redirect("all_active_books")
            else:
                return redirect("login_user")
        else:
            return redirect("login_user")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect("login_user")







from django.views.generic import View
from django.contrib.auth import forms


class LoginPageView(View):
    template_name = 'login.html' # instance variables
    form_class = AuthenticationForm
    
    def get(self, request):
        print("in get method")
        form = self.form_class()
        return render(request, self.template_name, context={'login_form': form})
        
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            print("in valid?")
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home_page')
        return render(request, self.template_name, context={'login_form': form})

