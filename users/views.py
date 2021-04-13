from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RegisterForm
from .models import Contact
from openings import models

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get("username")
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form= RegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profilepage(request):
    openings = Contact.objects.filter(user_from=request.user).values_list('user_to_id',flat=True)
    openings = models.Opening.objects.filter(pk__in=openings)

    categories = models.Categories.objects.all()
    opening_title = request.GET.get('opening_title')
    opening_category = request.GET.get('opening')
    if opening_category != "Default":
        categories_type = models.CategoriesTypes.objects.all().filter(category=opening_category)
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

    paginator = Paginator(openings,6)
    page = request.GET.get('page')
    openings = paginator.get_page(page)

    return render(request,'users/profile.html',{'openings':openings,'categories':categories,"categories_type":categories_type,})

@login_required
def delete_follow(request, id_opening):
    opening_followed = get_object_or_404(Contact,user_from =request.user.id, user_to=id_opening)
    opening_followed.delete()
    return redirect('profile')

@login_required
def add_follow(request, id_opening):
    obj, created = Contact.objects.get_or_create(user_from=request.user, user_to=models.Opening(pk=id_opening),)
    return redirect('profile')
