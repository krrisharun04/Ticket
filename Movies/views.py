from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
#from django.http import HttpResponse
from .models import Movie
from django.contrib.auth.models import User, auth

def index(request):
        p=Movie.objects.all()
        return render(request,'index.html',{'p':p})

# Create your views here.


def mdetails(request,moviename):
        moviedetails = Movie.objects.filter(mname=moviename)
        return render(request, 'mdetails.html', {"moviedetails": moviedetails})
def seat(request,moviename):
        # if request.method == 'POST':
        #         count=request.POST['count']
        #         total=request.POST['total']
        #         request.session['count'] =count
        #         request.session['total']=total
        #         print("count",count,total)
        #         return redirect(payment(request,moviename))
        moviedetails = Movie.objects.filter(mname=moviename)
        return render(request, 'seat.html', {"moviedetails": moviedetails})
def payment(request,moviename):
        moviedetails = Movie.objects.filter(mname=moviename)
        # if request.method=='POST':
        #         tpk=request.POST['setc']
        #         print('this is',tpk)
        # else:
        #         return redirect(details(request,moviename=moviedetails))
        
        # # if request.method=='GET':

        return render(request,'payment.html', {"moviedetails": moviedetails})
def details(request,moviename):
        moviedetails = Movie.objects.filter(mname=moviename)
        return render(request,'details.html', {"moviedetails": moviedetails})

def print(request,moviename):
        # count = request.session.get('count')
        # total = request.session.get('total')

        moviedetails =Movie.objects.filter(mname=moviename)
        return render(request,'print.html', {"moviedetails": moviedetails})
def login(request):
        if request.method=='POST':
                user=request.POST['username']
                password=request.POST['password']
                usr=auth.authenticate(username=user,password=password)
                if usr is not None:
                        auth.login(request,usr)
                        request.session['user']=user
                        return redirect(index)
                else:
                        messages.info(request,'invalid details')
                        return render(request,'login.html')
        return render(request,'login.html')

def registor(req):
    if req.method == 'POST':
        email = req.POST['email']
        name = req.POST['name']
        pwd1 = req.POST['password']
        pwd2 = req.POST['password1']

        if User.objects.filter(username=email).exists():
            messages.info(req, 'user taken')
            return render(req, 'registor.html')
        if pwd1 != pwd2:
            messages.info(req, 'password not matched')
            return render(req, 'registor.html')

        if User.objects.filter(email=email).exists():
            messages.info(req, 'Email Taken')
        # elif User.objects.filter(email=email).exists():

            return render(req, 'registor.html')

        else:
            user = User.objects.create_user(username=email, password=pwd1,
                                            email=email, first_name=name)
            user.save()
            messages.info(req, 'created success')
            return redirect(login)

    else:
        return render(req, 'registor.html')


def logout(request):
    auth.logout(request)
    return redirect(index)
