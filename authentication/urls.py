from django.urls import path
from django.contrib.auth import views as auth_views
from . views import SignupView


app_name = 'authentication'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="authentication/login.html"), name='login')
]