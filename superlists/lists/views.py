from django.shortcuts import redirect, render

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

# def home_page(request):
#     item = Item()
#     item.text = request.POST.get('item_text', '')
#     item.save()
#     # return render(request, 'home.html' {new_item_text: 'request.POST['item_text']'})
#     # return render(request, 'home.html', {'new_item_text': request.POST['item_text'],})
#     # return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''),}) 
#     return render(request, 'home.html', {'new_item_text': item.text,})

# def home_page(request):
#     if request.method == 'POST':
#         new_item_text = request.POST['item_text']
#         Item.objects.create(text=new_item_text)     
#     else:
#         new_item_text = ''

#     return render(request, 'home.html', {'new_item_text': new_item_text,})

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#     # return ('/')
#         return redirect('/')
#     items = Item.objects.all()
#     return render(request, 'home.html', {'items': items})

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
    # return ('/')
        return redirect('/lists/the-only-list-in-the-world/')
    # items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items}) 

def new_list(requests):
    Item.objects.create(test=request.POST['text_item'])
    # return render(request, '', {'items': items})  
    return redirect('/lists/the-only-list-in-the-world/')  
