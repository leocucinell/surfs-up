from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


#landing page
def landing_page(request):
    return render(request, 'landingpage.html', {})

#login page
def login_page(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        #TODO: Error handling in a else: block
    return render(request, 'login.html', {})

#signup page
def signup_page(request):
    form = CreateUserForm #This is the UserCreation form overwritten in the models file

    #This saves the form in django backend
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"account created for {user}")
            return redirect("login_page")

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

#home page
def home_page(request):
    return render(request, 'home.html', {})

#blog post page
def blog_post_page(request):
    return render(request, 'blogpost.html', {})

#create blog post page
def create_blog_post_page(request):
    return render(request, 'createblogpost.html', {})

# user page
def user_page(request):
    return render(request, 'user.html', {})

#about page
def about_page(request):
    return render(request, 'about.html', {})