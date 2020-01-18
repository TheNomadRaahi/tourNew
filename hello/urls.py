from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	#path('login/',views.LoginView.as_view(),name='login'),
    path('', views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login1,name="login1"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('shimla/',views.shimla,name="shimla"),
	path('dalhousie/',views.dalhousie,name="dalhousie"),
	path('kinnaur/',views.kinnaur,name="kinnaur")
]