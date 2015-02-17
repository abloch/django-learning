from django.shortcuts import render
from finder.models import Business
# Create your views here.
def index(request):
	b=Business.objects.all()
	return render(request,"finder/business.html",{'business':b})