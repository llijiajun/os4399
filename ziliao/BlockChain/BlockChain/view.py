from django.http import HttpResponse
from django.shortcuts import render
import time
import base64
import hmac
import urllib.request
import urllib.parse
import json
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

token=""

def login(request):
    token=get_token()
    fl=open("token.txt",'w')
    fl.write(token)
    fl.close()
    return render(request,'../templates/login.html')
def register(request):
    return render(request,'../templates/register.html',{'BLOCK_TOKEN':token})
def order(request):
    fl=open("token.txt",'r')
    token=fl.read()
    fl.close()
    return render(request,'../templates/order.html',{'BLOCK_TOKEN':token})
def trans(request):
    fl=open("token.txt",'r')
    token=fl.read()
    fl.close()
    return render(request,'../templates/trans.html',{'BLOCK_TOKEN':token})
def check(request):
    fl=open("token.txt",'r')
    token=fl.read()
    fl.close()
    return render(request,'../templates/check.html',{'BLOCK_TOKEN':token})
def get_token():
    url = 'http://101.201.67.133:4000/users'
    #准备一下头
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    values = {'username':'Jim','orgName':'Org1'}
    data = urllib.parse.urlencode(values).encode('utf-8')
    #创建一个request,放入我们的地址、数据、头
    request = urllib.request.Request(url, data, headers)
    #访问
    html = urllib.request.urlopen(request).read().decode('utf-8')
    #利用json解析包解析返回的json数据 拿到翻译结果
    token=json.loads(html)['token']
    return token
def get_data(request):
    order=request.POST.getlist('order_id')[0]
    try:
        fl=open(order+".txt",'r')
        d=fl.read()
        fl.close()
        return JsonResponse({"success": 1,"order":d})
    except:
        return JsonResponse({"success": 0,"order":""})
def write_order_data(request):
    order=request.POST.getlist('order_id')[0]
    da={'order_id':request.POST.getlist('order_id')[0],
        'order_name':request.POST.getlist('order_name')[0],
        'order_position':request.POST.getlist('order_position')[0],
        'order_telephone':request.POST.getlist('order_telephone')[0],
        'other_info':request.POST.getlist('other_info')[0],
        'order_company':request.POST.getlist('order_company')[0],
        'order_type':request.POST.getlist('order_type')[0],
        'order':request.POST.getlist('order')[0]}
    #try:
    fl=open(order+".txt",'w')
    fl.write(json.dumps(da))
    fl.close()
    return JsonResponse({"success": 1})
    #except:
    #    return JsonResponse({"success": 0})
def write_trans_data(request):
    order=request.POST.getlist('order_id')[0]
    da={'order_position':request.POST.getlist('order_position')[0],
        'order_num':request.POST.getlist('order_num')[0],
        'next_position':request.POST.getlist('next_position')[0],
        'other_info':request.POST.getlist('other_info')[0],
        'order_company':request.POST.getlist('order_company')[0],
        'order_type':request.POST.getlist('order_type')[0],
        'order_id':request.POST.getlist('order_id')[0],
        'order':request.POST.getlist('order')[0]}
    try:
        fl=open(order+".txt",'w')
        fl.write(json.dumps(da))
        fl.close()
        return JsonResponse({"success": 1})
    except:
        return JsonResponse({"success": 0})
