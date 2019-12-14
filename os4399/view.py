from django.shortcuts import render

def Index(request):
	context={}
	context['hello']='Hello World!'
	return render(request,'hello.html',context)