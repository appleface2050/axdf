#coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from util.basemodel import JSONBaseModel
from django.utils import timezone


class SMSCodeSession(JSONBaseModel):
    tel = models.CharField(default="", max_length=64, unique=False, null=False)
    code = models.CharField(default="", max_length=64, unique=False, null=False)
    uptime = models.DateTimeField(auto_now=True, verbose_name=u'数据更新时间')

    @classmethod
    def add(cls, tel, code):
        a = cls()
        a.tel = tel
        a.code = code
        try:
            a.save()
            return True
        except Exception, e:
            print e
            return False

    @classmethod
    def check_code_by_tel(cls, tel, code):
        if cls.objects.filter(tel=tel, code=code).exists():
            _code = cls.objects.filter(tel=tel, code=code).order_by('-uptime')[0].code
            if _code == code:
                cls.objects.filter(tel=tel, code=code).delete()
                return True
        return False


class Talk(JSONBaseModel):
    """
    交流
    """
    tel = models.CharField(default="", max_length=64, unique=False, null=False)
    text = models.CharField(default="", max_length=640, unique=False, null=False)
    uptime = models.DateTimeField(auto_now =True, verbose_name=u'数据更新时间')

    @classmethod
    def get_last_N_talk(cls, N=10):
        result = []
        data = cls.objects.all().order_by('-uptime')[:N]
        for i in data:
            result.append(i.toJSON())
        return result

    @classmethod
    def add_talk(cls, tel, text):
        a = cls()
        a.tel = tel
        a.text = text
        try:
            a.save()
            return True
        except Exception, e:
            print e
            return False


