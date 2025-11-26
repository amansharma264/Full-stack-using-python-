"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# In urls.py (just to double-check)
from django.urls import path
from basics import views

from django.urls import path
from basics import views

urlpatterns = [
    path("abc/", views.abc, name='abc'),
    path("led/", views.led, name='led'),
    path("counter/", views.counter, name='counter'),
    path("calci/", views.calci, name='calci'),
    path("department/", views.department, name='department'),
    path("departmentview/", views.departmentview, name='departmentview'),
    path("departmentupdate/<int:id>/", views.departmentupdate, name='departmentupdate'),
    path("departmentdelete/<int:id>/", views.departmentdelete, name='departmentdelete'),
]


