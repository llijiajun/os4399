"""BlockChain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^$', view.login),
    url(r'^templates/login$', view.login),
    url(r'^templates/register$', view.register),
    url(r'^templates/order$', view.order),
    url(r'^templates/trans$', view.trans),
    url(r'^templates/check$', view.check),
    url(r'^templates/get_data$',view.get_data),
    url(r'^templates/write_order_data$',view.write_order_data),
    url(r'^templates/write_trans_data$',view.write_trans_data),
]
