from django.shortcuts import render,HttpResponse
from django.views import View
from .models import AddProf,about

#THus is the Clas Based View of main/home page of the website
class HomePage(View):
	def get(self,request):
		add = AddProf.objects.all()
		About = about.objects.all()
		return render(request,'index.html',{'addprof':add,'about':About})

def soon(request):
	return HttpResponse("<h1>Comming soon....</h1")
