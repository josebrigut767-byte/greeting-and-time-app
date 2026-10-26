"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from greetingApp import views as greeting_views
from timeApp import views as time_views
from quoteApp.views import motivation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', greeting_views.greetings_view),
    path('welcome/', greeting_views.welcome_view),
    path('motivation/', motivation_view),
    path('time/', time_views.time_info_view),
    path('date/', time_views.date_info_view),
    path('worldclock/', time_views.world_clock_view),
    path('birthday/', greeting_views.birthday_view),
]
