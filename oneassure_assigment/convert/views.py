from django.http import JsonResponse
from django.shortcuts import render
from .models import Data
import json

# Create your views here.

def home(request):
  all_data=Data.objects.all()
  ls=[]
  for obj in all_data:
    temp=[]
    temp.append(obj.id)
    for key,value in obj.json_data.items():
      temp.append(key)
    ls.append(temp)
  return render(request,'home.html',{'ls':ls})
  
  #return HttpResponse("Hello")



def post_data(request):
  file_data = json.loads(request.POST['data'])##this convert json string into python data structure
  Data.objects.create(json_data=file_data)
  return JsonResponse({"message":"ok"})




