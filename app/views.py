from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'app/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo':photo}
    return render(request, 'app/photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()
    context = {'categories':categories,}
    return render(request, 'app/add.html', context)
