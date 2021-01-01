from django.shortcuts import render,redirect
from helmet.models import Helmet
from helmet.forms import HelmetForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    helmet=Helmet.objects.raw("select * from helmet limit 4 offset %s",[offset])
    pageItem=len(helmet)
    return render(request,"helmet/index.html",{'helmet':helmet,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=HelmetForm(request.POST,request.FILES)
        form.save()
        return redirect("/helmet")
    else:
        form=HelmetForm()
    return render(request,"helmet/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    helmet=Helmet.objects.get(helmet_id=id)
    if request.method=="POST":
        form=HelmetForm(request.POST,request.FILES,instance=helmet)
        form.save()
        return redirect("/helmet")
    else:
        form=HelmetForm(instance=helmet)
    return render(request,"helmet/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    helmet=Helmet.objects.get(helmet_id=id)
    helmet.delete()
    return redirect("/helmet")