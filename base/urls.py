from django.urls import path

from .views import landing_page, login_page, signup_page, home_page, blog_post_page, create_blog_post_page, user_page, about_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_page, name='login_page'),
    path('signup/', signup_page, name='signup_page'),
    path('home/', home_page, name='home_page'),
    path('post/<int:pk>/', blog_post_page, name='blog_post_page'),
    path('post/create/', create_blog_post_page, name='create_blog_post_page'),
    path('user', user_page, name='user_page'),
    path('about', about_page, name='about_page')
]