from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, StreamingHttpResponse
from multiprocessing import Pool
from managementcenter.views import globeFunction
from managementcenter.views import peopleManage,employeeManage,volunteerManage


# 增加用户信息
def addPeopleInfo(request):
    result = peopleManage.addOldInfo(request)
    return JsonResponse(result, safe=False)

# 更新用户信息
def updatePeopleInfo(request):
    result = peopleManage.updateOldInfo(request)
    return JsonResponse(result, safe=False)

# 用户退订办理
def checkoutPeople(request):
    result = peopleManage.checkoutOld(request)
    return JsonResponse(result, safe=False)

# 根据id查询用户信息
def checkPeopleById(request):
    result = peopleManage.checkOldById(request)
    return JsonResponse(result, safe=False)

# 获取所有用户信息
def getPeopleList(request):
    result = peopleManage.getOldList(request)
    return JsonResponse(result, safe=False)

# 获取用户数量
def getPeopleNum(request):
    result = peopleManage.getOldNum(request)
    return JsonResponse(result, safe=False)

# 用户年龄分布直方图
def getPeopleAgeNum(request):
    result = peopleManage.getOldAgeNum(request)
    return JsonResponse(result, safe=False)
