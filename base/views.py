from django.shortcuts import render

#landing page
def landing_page(request):
    return render(request, 'landingpage.html', {})

#login page
def login_page(request):
    return render(request, 'login.html', {})

#signup page
def signup_page(request):
    return render(request, 'signup.html', {})

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