# -*- coding:utf-8 -*-
from django.http import HttpResponse
import json


def getSpeed(request):
    try:
        print ("hello")
        u = int(request.GET.get('u'))
        print ("bbb")
        i = int(request.GET.get('i'))
        print ("ccc")
        print (u)
        print (i)
        if u > 2000 or u< -2000:
            return HttpResponse('参数错误，请检查参数U，范围-2000~2000')
        print ("ddd")
        if i <= 0 or i > 2000:
            return HttpResponse('参数错误，请检查参数I，范围0~2000')
        p = int(u * i)
        print (p)
        n = 0
        if abs(p) > 300000:
            n = 3000
        elif abs(p) > 30000:
            n = 1500
        elif abs(p) > 3000:
            n = 1000
        elif abs(p) > 300:
            n = 750
        else:
            n = 600
        print n
        return HttpResponse('输入电压：' + str(u) + 'V</br>输入电流：' + str(i) + 'A</br>计算功率：' + str(p) + 'W</br>计算转速：' + str(n))
    except:
        return HttpResponse('参数错误，请检查参数，访问地址应该为http://[服务器地址]:[服务器端口号]/getSpeed?U=220&I=36')
