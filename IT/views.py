from django.shortcuts import render
from .models import ServiceData


# Create your views here.
def test(request):
    try:
        #obj = ServiceData.object.get(id=1)
        obj = ServiceData.objects.all
        return render(request, 'index.html', {'object': obj})
    except:
        return render(request, 'index.html')
    #except Exception as e:
       #print(e)
        #return render(request, 'index.html')

def register(request):
    if request == "POST":
        a = request.POST['form_head']
        b = request.POST['form_des']
        ServiceData.objects.create(head=a,des=b,img=None)
        #print(a,b)
        #print(request)
        #ServiceData.objects.filter()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def search(request):
    data = request.GET['search']
    objects = ServiceData.objects.filter(head=data)
    print(objects)
    return render(request, 'search.html', {'obj': objects})

def delete(request):
    ServiceData.objects.get(id=pk).delete()
    return redirect('services')

def test():
    test
