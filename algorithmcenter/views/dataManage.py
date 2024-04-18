import datetime
import json

from django.core import serializers
from django.forms import model_to_dict
from django.utils import timezone
import pytz

import managementcenter.models
from managementcenter.views import globeFunction
from algorithmcenter import models
from django.core.cache import cache
from django.shortcuts import render, HttpResponse
import time
from django.views.decorators.cache import cache_page

def get_now_time():
    """获取当前时间"""
    tz = pytz.timezone('Asia/Shanghai')
    # 返回时间格式的字符串
    now_time = timezone.now().astimezone(tz=tz)
    now_time_str = now_time.strftime("%Y.%m.%d %H:%M:%S")
    # 返回datetime格式的时间
    now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    return now

def addEvent(oldPersonId, event_type, event_desc,event_place):
    now = get_now_time()
    try:
        event = models.event_info(oldperson_id=oldPersonId, event_desc=event_desc,
                                  event_type=event_type, event_date=now, event_place=event_place, status=0)
        event.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    print("addEvent 被调用")
    return {'msg': '添加成功', "code": '200'}

def getEventInfo(request):
    try:
        event_list = models.event_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in event_list:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'eventList': res}

def changeEventStatus(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]
    try:
        models.event_info.objects.filter(ID=id).update(status=1)
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    return {'msg': '更新成功', "code": '200'}

