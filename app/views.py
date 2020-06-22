from django.shortcuts import render, redirect, get_object_or_404
from .forms import New_Tag, New_Item
from .models import *

# Create your views here.
def home(request):
    #item = search_item(request)
    item_search = request.GET.get('search_item', None)
    tag_search = request.GET.get('itens_tags', None)

    if item_search or tag_search:
        item = Item.objects.filter(name__icontains=item_search)
        if tag_search:
            if(tag_search != 'all'):
                item = item.filter(tag = tag_search)
        print(item)
    else:
        item = Item.show_datas(Item)
    all_tags = Tag.show_all_tags(Tag)
    #I'm passing variables in the dictionary: first is the Item, second is the Tags
    return render(request,'home.html',{'itens': item,'all_tags':all_tags})

def item_description(request, id):
    #If don't exist any Item, it return an Erro 404
    item = get_object_or_404(Item, pk=id)

    #There is a Modal in the template to update the item
    #form gets an instence of NewItem and fill in all fields of form
    form = New_Item(request.POST or None, request.FILES or None, instance=item)
    complete_form = update_item(form)

    return render(request,'item_description.html',{'item':item,'form':complete_form})


def new_item(request):
    #Register a new item in DB

    #form get the requests in format POST  (form get an istance of NewItem)
    form = New_Item(request.POST or None, request.FILES or None)

    if form.is_valid():
        #Save in DB this new item
        form.save()
        #Redirect to a url
        return redirect('url_home')
    #render needs to pass the request, tamplate and sometimes a dictionary of variables
    return render(request,'new_item.html', {'form': form})

def update_item(form):
    if form.is_valid():
        #if form is correct, save in DB
        form.save()
    return form


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('url_home')

def new_item_tag(request):
    form = New_Tag(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request,'new_item_tag.html',{'form':form})

def search_item():
    pass