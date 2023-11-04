from django.urls import path
import web.views as views

urlpatterns = [
    path('', views.UserLogin.as_view(), name='login_page'),
    path('logout', views.UserLogOut.as_view(), name='logout_page'),
    path('index', views.index, name='index'),
]
