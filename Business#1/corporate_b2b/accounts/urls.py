from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        extra_context={'site_name': 'Ambro Bites'}
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registration
    path('signup/', views.signup, name='signup'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
]