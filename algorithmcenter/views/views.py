from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, StreamingHttpResponse

import algorithmcenter
from algorithmcenter.views import dataManage
from algorithmcenter.views.voiceChat import chatgpt

def test01(request):
    result = dataManage.addEvent(2,"污染","污染")
    return JsonResponse('test02', safe=False)

# 获取事件列表
def getEventInfo(request):
    result = dataManage.getEventInfo(request)
    return JsonResponse(result, safe=False)

def changeEventStatus(request):
    result = dataManage.changeEventStatus(request)
    return JsonResponse(result, safe=False)

def getChatResult(request):
    result = chatgpt.ChatGPT(request)
    return JsonResponse(result, safe=False)

def addCallEvent(request):
    result = dataManage.addNewCall(request)
    return JsonResponse(result, safe=False)

