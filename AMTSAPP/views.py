from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def homeView(request):
	return render(request,'index.html')

def blogView(request):
	return render(request,'blog.html')

def contactView(request):
	return render(request,'contact.html')

def passView(request):
	return render(request,'Pass.html')

def servicesView(request):
	return render(request,'services.html')

def creaatepasspage(request):
	return render(request,'createpass.html')

def createpass(request):
	select=request.POST['select']
	if select=="student":
		return render(request,'Studentpass.html')
	elif select=="job":
		return render(request,'JobPass.html')
	elif select=="senior":
		return render(request,'SeniorCitizenPass.html')

def studentpass(request):
	return render(request,'Studentpass.html')

def jobpass(request):
	return render(request,'JobPass.html')

def seniorcitizenpass(request):
	return render(request,'SeniorCitizenPass.html')

def saveStudentView(request):
	data=StudentModel()
	data.cname=request.GET['cname']
	data.ccourse=request.GET['ccourse']
	data.cyear=request.GET['cyear']
	data.cphoto=request.GET['cphoto']
	data.cfees=request.GET['cfees']
	data.save()
	return render(request,'LastPage.html')	

def saveJobView(request):
	data=JobModel()
	data.jname=request.GET['jname']
	data.jaddress=request.GET['jaddress']
	data.jletter=request.GET['jletter']
	data.save()
	return HttpResponse("Data Inserted")

def saveSeniorCitizenView(request):
	data=SeniorCitizenModel()
	data.scname=request.GET['scname']
	data.scage=request.GET['scage']
	data.save()
	return HttpResponse("Data Inserted")