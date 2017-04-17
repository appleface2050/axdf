# coding=utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import Talk, SMSCodeSession
from util.jsonresult import getResult
from yunpian.SmsOperator import SmsOperator
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import json

def index(request):
    return HttpResponse("Hello, world. axdf")

@csrf_exempt
def talk(request):
    if request.method == "POST":
        tel = request.POST.get("tel", None)
        text = request.POST.get("text", "")
        if not tel:
            return getResult(False, "tel is none")
        if not text:
            return getResult(False, "text is empty")
        result = Talk.add_talk(tel,text)
        if result:
            return getResult(True, "post talk success")
        else:
            return getResult(False, "post talk fail")


    elif request.method == "GET":
        talk = Talk.get_last_N_talk(10)
        return getResult(True, "get talk success", talk)


def send_sms_code(request):
    # tel = request.REQUEST.get("tel")
    tel = request.GET.get("tel", 0)
    try:
        telnum = int(tel)
        if telnum < 10000000000 or telnum > 20000000000:
            return getResult(False, u'手机号不正确', None)
    except:
        return getResult(False, u'手机号不正确', None)
    if tel:
        if request.session.has_key("sms_num_%s" % str(tel)):
            num = request.session["sms_num_%s" % str(tel)]
        else:
            num = 0
        if request.session.has_key("sms_sendtime_%s" % str(tel)):
            sendtime = request.session["sms_sendtime_%s" % str(tel)]
        else:
            sendtime = None
        from datetime import datetime

        if sendtime:
            sendtime = datetime(int(sendtime[:4]), int(sendtime[4:6]), int(sendtime[6:8]), int(sendtime[8:10]),
                                int(sendtime[10:12]), int(sendtime[12:14]))
            if (datetime.now() - sendtime).seconds < 60:
                return getResult(False, u'每分钟只能发送一次验证码', None)
        else:
            num = 0
        import random

        code = random.randint(1000, 9999)
        request.session["smscode"] = str(code)
        request.session["smstel"] = str(tel)
        request.session["sms_num_%s" % str(tel)] = num + 1
        request.session["sms_sendtime_%s" % str(tel)] = datetime.now().strftime("%Y%m%d%H%M%S")
        print code

        APIKEY = '75a9b2a5ec2ed31ac7f7d5bdbe183a3e'
        smsOperator = SmsOperator(APIKEY)
        result = smsOperator.single_send({'mobile': str(tel), 'text': '【安新电服】您的验证码是%s'% str(code)})
        # result = smsOperator.single_send({'mobile': str(tel), 'text': '【安新电服】您的验证码是:%s' % str(code)})
        print json.dumps(result.content, ensure_ascii=False)
        if result.status_code == 200 and SMSCodeSession.add(tel,code):
            return getResult(True, u'sms send success', None)
        else:
            return getResult(False, result.content.get("msg",""), None)
    else:
        return getResult(False, u'one minute one time', None)

