
from django.urls import path
from .views import  register_user,login_page,logout_page
urlpatterns = [
    path("register",register_user,name="register"),
    path("login",login_page,name="login"),
    path("logout",logout_page,name="logout")
]
