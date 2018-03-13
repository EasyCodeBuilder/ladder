from django.http import HttpResponse
from .dao.User import *

def hello(request):
    json={"name":"lyk","no":"12548"}
    return HttpResponse(json)

def manage(request):
    data=request.GET['data']
    type=request.GET['type']
    print(type)

    if(type=="adduser"):
        data=""


    elif (type=="addacct"):

        data = ""
    return HttpResponse("manage")