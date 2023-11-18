
from django.contrib import admin
from django.urls import path
from BlogApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('login/', LoginForm, name="loginform"),
    path('logout/', Logoutuser, name="logout"),
    path('signup/', Signup, name="signup"),
    path('single/<int:bid>/', Blogdetail, name="detail"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)