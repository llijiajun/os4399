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
	return render(request,'../templates/index.html')

def Wuzi(request):
	return render(request,'../templates/wuzi.html')

def zhuye(request):
	return render(request,'../templates/zhuye.html')

def dadishu(request):
	return render(request,'../templates/dadishu.html')

def dafeiji(request):
	return render(request,'../templates/dafeiji.html')

def feiji(request):
	return render(request,'../templates/feiji.html')