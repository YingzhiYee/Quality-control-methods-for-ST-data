from django.urls import path

from algorithmcenter.views import views as care_views

urlpatterns = [
    path('getEventList/', care_views.getEventInfo),
    # path('areaChoose/', care_views.areaChoose), # 污染区域选择
    path('getIntrusionStream/', care_views.getIntrusionStream),  # 污染检测
    path('getspotclean/', care_views.getspotclean),  # spotclaen算法

    path('changeEventStatus/', care_views.changeEventStatus),
    path('getChatContent/', care_views.getChatResult),
    path('addNewCall/', care_views.addCallEvent),

]