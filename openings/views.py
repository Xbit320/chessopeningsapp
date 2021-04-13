from django.shortcuts import render
from .models import Opening, Categories, CategoriesTypes
from django.core.paginator import Paginator
from users import models

# Create your views here.
def opening_bar(request):

    openings = Opening.objects.all()
    categories = Categories.objects.all()
    categories_type = CategoriesTypes.objects.all()

    opening_title = request.GET.get('opening_title')
    
    opening_category = request.GET.get('opening')
    if opening_category != "Default":
        categories_type = CategoriesTypes.objects.all().filter(category=opening_category)
    else:
        categories_type = []

    opening_category_type = request.GET.get('opening_type')
    if opening_category_type is None:
        opening_category_type = "Default"

    if opening_title != '' and opening_title is not None :
        if opening_category != "Default":
            if opening_category_type != "Default":
                openings = openings.filter(title__icontains=opening_title,category_type=opening_category_type)
            else:
                openings = openings.filter(title__icontains=opening_title,category=opening_category)
        else:
            if opening_category_type != "Default":
                openings = openings.filter(title__icontains=opening_title,category_type=opening_category_type)
            else:
                openings = openings.filter(title__icontains=opening_title)
    else:
        if opening_category != "Default" and opening_category != '' and opening_category is not None:
            if opening_category_type != "Default" and opening_category_type != '' and opening_category_type is not None:
                openings = openings.filter(category_type=opening_category_type)
            else:
                openings = openings.filter(category=opening_category)
        else:
            if opening_category_type != "Default" and opening_category_type != '' and opening_category_type is not None:
                openings = openings.filter(category_type=opening_category_type)

    if opening_category != "Default":
        categories_type = CategoriesTypes.objects.all().filter(category=opening_category)
    else:
        categories_type = []

    paginator = Paginator(openings,6)
    page = request.GET.get('page')
    openings = paginator.get_page(page)  
    return render(request,'openings/index.html',{'openings':openings,'categories':categories, "categories_type":categories_type,})


def detail(request,id):
    if request.user.is_authenticated:
        openings = models.Contact.objects.filter(user_from=request.user).values_list('user_to_id',flat=True)
        if id in openings:
            followed = 1
        else:
            followed = 0
    else:
        followed = "ANON"
    embed_code = Opening.objects.get(pk=id).embed_code
    has_puzzle = 1

    return render(request,'openings/detail.html',{'embed_code':embed_code, "id":id, "followed":followed, "has_puzzle" :has_puzzle})

def opening_puzzle(request,id):
    if request.user.is_authenticated:
        openings = models.Contact.objects.filter(user_from=request.user).values_list('user_to_id',flat=True)
        if id in openings:
            followed = 1
        else:
            followed = 0
    else:
        followed = "ANON"
    embed_code = Opening.objects.get(pk=id).embed_code_chess_com

    has_puzzle = 0

    return render(request,'openings/detail.html',{'embed_code':embed_code, "id":id, "followed":followed, "has_puzzle":has_puzzle})
