from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Basic_Itineraries
# Create your views here.
def index(request):
	return render(request,'hello/first.html')

def contact(request):
	return render(request,'hello/contact.html')

def signup(request):
	thank=False
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			thank=True
			username=form.cleaned_data.get('username')
			request.session['username']=username
			params={'thank':thank,'user':username}
			return render(request,'hello/first.html',params)
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})

def login1(request):
	thank1=False
	thank2=False
	thank3=False
	if(request.method=='POST'):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user1=authenticate(username=username,password=password)
		if user1 is not None:
			if user1.is_active:
				thank1=True
				request.session['username']=username
				params={'thank1':thank1,'user':username}
				return render(request,'hello/first.html',params)
			else:
				thank2=True
		else:
			thank3=True
			return render(request,'registration/login.html',{'thank3':thank3})
	params={'thank2':thank2,'thank3':thank3}
	return render(request,'registration/login.html',params)

def shimla(request):
	thank=False
	th=Basic_Itineraries.objects.get(it_id=1002)
	if(request.session.has_key('username')):
		thank=True
		param={'thank':thank,'user':request.session['username'],'th':th}
		return render(request,'hello/shimla.html',param)
	else:
		return render(request,'registration/login.html')

def dalhousie(request):
	thank=False
	th=Basic_Itineraries.objects.get(it_id=3003)
	if(request.session.has_key('username')):
		thank=True
		param={'thank':thank,'user':request.session['username'],'th':th}
		return render(request,'hello/shimla.html',param)
	else:
		return render(request,'registration/login.html')
		
def kinnaur(request):
	thank=False
	th=Basic_Itineraries.objects.get(it_id=2004)
	if(request.session.has_key('username')):
		thank=True
		param={'thank':thank,'user':request.session['username'],'th':th}
		return render(request,'hello/shimla.html',param)
	else:
		return render(request,'registration/login.html')
		

