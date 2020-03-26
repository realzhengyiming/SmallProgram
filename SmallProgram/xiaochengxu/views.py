from django.shortcuts import render
from django.db import connection
from django.shortcuts import HttpResponse
import time
import json
from random import randrange
from django.http import HttpResponse
from rest_framework.views import APIView
from .tools_pakages import *
import os

# from django.db.models import Avg, Max, Min, Count, Sum  # 直接使用models中的统计类来进行统计查询操作
# Create your views here.
def fetchall_sql(sql)->dict:  # 这儿唯一有一个就是显示页面的
    # latest_question_list = KeyWordItem # 换成直接使用sql来进行工作
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchall()[:100]
        # columns = [col[0] for col in cursor.description]  # 提取出column_name
        # return [dict(zip(columns, row)) for row in cursor.fetchall()][0]
        return row


def index(request):  # 这儿唯一有一个就是显示页面的
    print()
    return HttpResponse("这个是response")


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error

# 这个是 登陆,不用这种，这种是高耦合
# def login(request):
#     if request.method == 'GET':
#         print("get进来的")
#         return HttpResponse("fuck you ")
#     if request.method == 'POST':  # 当提交表单时
#         print("post进来了")
#         dic = {"flag":1}  # 这个是什么东西
#         判断是否传参
#         # if request.POST:
#         #     password = request.POST.get('password')
#         #     account = request.POST.get('account')
#             判断参数中是否含有a和b
#             # print(password)
#             # print(account)
#             # return HttpResponse(dic)
#         else:
#         # return HttpResponse('输入错误')
#
#     else:
#         return HttpResponse('方法错误')
class course_get(APIView):  # 使用不同的试图来进行封装
    def get(self,request,*args,**kwargs):
        # return Response("fuck")
        password = self.request.query_params.get("password")
        username = self.request.query_params.get("account")
  

        checkPath(os.path.dirname(__file__)+"/cookieData")        # return Response(userSerializer.data)
        return JsonResponse({"data":getCourseByCookie('17034480220'),"result":os.path.dirname(__file__)})
        
    def post(self,request,*args,**kwargs):
        password = self.request.query_params.get("password")
        username = self.request.query_params.get("account")
        print("port")
        print(password)
        print(username)
        user = User.objects.filter(username=username,password=password).first()

        return JsonResponse({"result":user.data})



