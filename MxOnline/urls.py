# coding:utf-8
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

# TemplateView：专门用来处理静态文件,不需要专门写一个view来映射.
from django.views.generic import TemplateView
import xadmin

from users.views import LoginView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    # url(r'^login/$', user_login, name="login"),
    url(r'^login/$', LoginView.as_view(), name="login")
]

'''
user_login和user_login()区别：
user_login代表指向这个函数
user_login()代表调用这个函数
LoginView.as_view():把LoginView类转换为一个as_view,返回一个函数句柄,此处要调用用方法，所以要()。
'''

