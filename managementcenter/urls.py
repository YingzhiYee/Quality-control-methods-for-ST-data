from django.urls import path

from managementcenter.views import views as manage_views

urlpatterns = [
    # 用户
    path('addPeople/', manage_views.addPeopleInfo),
    path('updatePeople/', manage_views.updatePeopleInfo),
    path('checkoutPeople/', manage_views.checkoutPeople),
    path('checkPeopleById/', manage_views.checkPeopleById),
    path('getPeopleList/', manage_views.getPeopleList),

    path('getPeopleAgeNum/', manage_views.getPeopleAgeNum),
    path('getPeopleNum/', manage_views.getPeopleNum),
]