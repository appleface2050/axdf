# coding=utf-8
from django.conf.urls import url

from app.views import send_sms_code, talk
from . import views
from views_user import sign_up, user_login, sign_out

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up$', sign_up, name='sign_up'),
    url(r'^sign_in$', user_login, name='sign_in'),
    url(r'^sign_out$', sign_out, name='sign_out'),
    url(r'^send_sms_code$', send_sms_code, name='send_sms_code'),
    url(r'^talk$', talk, name='talk'),

]