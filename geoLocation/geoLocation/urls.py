from django.contrib import admin
from django.urls import path
from .views import dashboard, logout, report, profiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout, name="logout"),
    path('',dashboard, name="dashboard"),
    path('report/',report, name="report"),
    path('profiles/',profiles, name="profiles"),
]
