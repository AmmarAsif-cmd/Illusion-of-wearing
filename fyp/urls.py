"""fyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home),
    path('script',views.script ),
    path('Test',views.tst , name="sc"),
    path('shirt/<int:num>/',views.shirt),
    path('pant/<int:num>/',views.pant),
    path('glass/<int:num>/',views.glass),
    path('sleeveless/<int:num>/',views.sleeveless),
    path('punjabi/<int:num>/',views.punjabi),
    path('printed/<int:num>/',views.printed),
    path('didasha/<int:num>/',views.didasha),
    # path('hair/<int:num>/',views.hair),
    path('manual',views.manual )
]