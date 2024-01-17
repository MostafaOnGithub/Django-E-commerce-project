from django.contrib import admin
from django.urls import path,include
from api.views import register_user, user_login, user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/',include('api.urls')),
]

