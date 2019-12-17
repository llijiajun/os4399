from django.shortcuts import render
from django.http import HttpResponse
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


def Index(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/index.html',{'user_id':""})
	else:
		return render(request,'../templates/index.html',{'user_id':userid[0]})

def Wuzi(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/wuzi.html',{'user_id':""})
	else:
		return render(request,'../templates/wuzi.html',{'user_id':userid[0]})

def zhuye(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/zhuye.html',{'user_id':""})
	else:
		return render(request,'../templates/zhuye.html',{'user_id':userid[0]})

def dadishu(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/dadishu.html',{'user_id':""})
	else:
		return render(request,'../templates/dadishu.html',{'user_id':userid[0]})

def dafeiji(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/dafeiji.html',{'user_id':""})
	else:
		return render(request,'../templates/dafeiji.html',{'user_id':userid[0]})

def feiji(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/feiji.html',{'user_id':""})
	else:
		return render(request,'../templates/feiji.html',{'user_id':userid[0]})

def chess(request):
	userid=request.GET.getlist('user_id')
	if len(userid)==0:
		return render(request,'../templates/chess.html',{'user_id':""})
	else:
		return render(request,'../templates/chess.html',{'user_id':userid[0],'room_id':request.GET.getlist('room_id')[0]})
