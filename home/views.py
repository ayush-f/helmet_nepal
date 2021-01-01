from django.shortcuts import render,redirect
from helmet.models import Helmet
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    helmet=Helmet.objects.all()
    return render(request,'home/index.html' ,{'helmet':helmet})

def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})

def login(request):
    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']
       print('done')

       return redirect("/user")

    return render(request,"home/login.html")

def logout(request):
    request.session.clear()
    return redirect("/")