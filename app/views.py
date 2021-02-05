from django.shortcuts import render

def gallery(request):
    return render(request, 'app/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'app/photo.html')

def addPhoto(request):
    return render(request, 'app/add.html')
