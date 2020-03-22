from django.shortcuts import render
from django.db import connection
from django.shortcuts import HttpResponse
# from .models import House
import time
# from django.db.models import Avg, Max, Min, Count, Sum  # 直接使用models中的统计类来进行统计查询操作

# Create your views here.
#  封装一个自动的游标来使用,todo 可能是这个有问题把，这个
def fetchall_sql(sql)->dict:  # 这儿唯一有一个就是显示页面的
    # latest_question_list = KeyWordItem # 换成直接使用sql来进行工作
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchall()[:100]
        # columns = [col[0] for col in cursor.description]  # 提取出column_name
        # return [dict(zip(columns, row)) for row in cursor.fetchall()][0]
        return row


def index(request):  # 这儿唯一有一个就是显示页面的
    return HttpResponse("这个是response")