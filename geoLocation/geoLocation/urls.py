from django.contrib import admin
from django.urls import path
from .views import dashboard, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout, name="logout"),
    path('',dashboard, name="dashboard"),
]
