from django.shortcuts import render
from app1.models import Movie
def home(request):
    k=Movie.objects.all()
    return render(request,'home.html',{'movie':k})
def addmovie(request):
    if request.method == "POST":
        t = request.POST['t']
        d = request.POST.get('d')
        y = request.POST['y']
        l = request.POST['l']
        i = request.FILES.get('i')

        m=Movie.objects.create(title=t,description=d,year=y,language=l,images=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def detail(request,i):
    k=Movie.objects.get(id=i)
    return render(request,'detail.html',{'movie':k})

def edit(request,i):
    k=Movie.objects.get(id=i)

    if request.method == "POST":
        k.title = request.POST['t']
        k.description = request.POST.get('d')
        k.year = request.POST['y']
        k.language = request.POST['l']

        if request.FILES.get('i') == None:
            k.save()
        else:
            k.cover = request.FILES.get('i')
        k.save()
        return home(request)

    return render(request,'edit.html',{'movie':k})


def delete(request,i):

    k = Movie.objects.get(id=i)
    k.delete()
    return home(request)
