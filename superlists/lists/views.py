from django.shortcuts import render

# # def index(request):
# #     render "Hello world"

# home_page = None

from django.http import HttpResponse
from lists.models import Item

# def home_page(request):
#     # return httpresponse(<h1> To Do List </h1>)
#     return HttpResponse('<html><Header>To-Do lists</Header><html>')

# def home_page(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST['item_text'])
#     return render(request, 'home.html')

def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    # return render(request, 'home.html' {new_item_text: 'request.POST['item_text']'})
    # return render(request, 'home.html', {'new_item_text': request.POST['item_text'],})
    # return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''),}) 
    return render(request, 'home.html', {'new_item_text': item.text,}) 

