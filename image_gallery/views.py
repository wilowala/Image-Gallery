from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image
import datetime as dt

# Create your views here.
def test(request):

    return render(request,'hello.html')

def home(request):
    date = dt.date.today()
    return render(request, 'index.html',{"date": date})

def gallery(request):
    my_gallery= Image.get_images()
    print(my_gallery)
    return render(request, 'gallery.html', {'gallery': my_gallery})


def search(request):
    if 'category_name' in request.GET and request.GET['category_name']:
        search_name = request.GET.get('category_name')
        searched_images = Image.search_image_by_cat(search_name)
       
        print(search_name)
               
        user_msg= f'{search_name}'
        return render(request, 'search.html', {'message':user_msg, 'images':searched_images})
    else:
        messages = "Please enter a keyword to search"
        return render(request,'search.html',{'message': messages})