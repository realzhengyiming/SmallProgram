# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     urls   
   Description :  
   Author :        zhengyimiing 
   date：          2020/1/10 
-------------------------------------------------
   Change Activity:
                   2020/1/10  
-------------------------------------------------
"""

__author__ = 'zhengyimiing'
from django.urls import path
from . import views

app_name = "xiaochengxu"    # 这儿需要设置这个来分辨不同的app

urlpatterns = [
    path("", views.index, name='index'),
    path("/course_get", views.course_get.as_view(), name="course_get"),

    # path('<int:page>/',views.page,name = 'page'),
    # /polls/  这种默认是在polls下的/

    # path('<int:question_id>/', views.detail, name="detail"),  # 命名的方式是为了方便后面的调用
    # {% url 'detail' questionnid %}
    # /polls/5/
#
    # path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/results/

    # path("<int:question_id>/vote/", views.vote, name="vote"),
    # /polls/5/vote/  投票的链接

    # path("<int:pk>/result/", views.ResultsView.as_view(), name="results")  # 这个是使用通用视图函数来进行操作

    # path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 配置上传图片可以访问的静态映射
]
