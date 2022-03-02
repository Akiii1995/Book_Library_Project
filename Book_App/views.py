import imp
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from .models import Book
# from django.http import HttpResponse

# def Homepage(request):          #-HTTP Request--all meta data come here
#     return HttpResponse("Welcome to Your First Website..!!!!!!")


# # http://127.0.0.1:8000/Home        -Base Url
# from .models import Book
# from django.http import HttpResponse


#function Based Views

# def homepage(request):
#     return HttpResponse("Welcome to First Website Akshay")
# from .models import Book
# from django.http import HttpResponse

def Homepage(requet):
    return HttpResponse("Welcome to the First........!!!!!!!!!!")

# def Homepage(request):
#     a = [1,2,3,4,5]
#     return HttpResponse(a)

# def Homepage(request):
#     pass

#     # print(dir(request))
#     # print(request.build_absolute_uri())

#     # return HttpResponse("<h1>I am Akshay Kumar<h1>\n<h2>I am good guy<h2>\n<h3>I am very genioun<h3>\n<h4>Mayura is good<h4>\n<h5>please do subscribe<h5>")
#     return render(request,"home.html")