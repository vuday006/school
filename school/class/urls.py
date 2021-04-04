from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views

router = DefaultRouter()

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('teacher_details/', views.teacher_details, name='teacher_details'),
    path('student_details/', views.student_details, name='student_details'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

]
