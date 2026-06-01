from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
    data={'title':'home | E_Luxuria_website'}
    return render(request,'index.html',data)
    
def About(request):
    return render(request,'About.html')

def Signin(request):
    if request.method == "POST":

        email = request.POST['email']
        Password = request.POST['Password']
        user = Register.objects.filter(email=email,Password=Password).first()
        if user is not None:
            request.session['email']=email
            
            return redirect('index')
           
            
        else:
            
            from django.contrib import messages
        messages.error(request,'Wrong email or password! Please try again.')
        return redirect('Signin')
            
            
    data={'title':'Login'}
    return render(request,'signin.html',data)
    

def Shop(request):
    products=Product.objects.filter(status=1)
    return render(request,'shop.html',{'products':products})



def Signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        Password = request.POST['Password']
        Mobile_No = request.POST['Mobile_No']
        Address= request.POST['Address']
        Gender= request.POST['Gender']
        Country = request.POST['Country']
        State = request.POST['State']
        PIN = request.POST['PIN']  
        data = Register.objects.create(name=name,email=email,Password=Password,Mobile_No=Mobile_No,Address=Address,Gender=Gender,Country=Country,State=State,PIN=PIN)
        return redirect('Signin')  

    return render(request,'signup.html')

def regis(request):
    li=Register.objects.all()
    #li=Register.objects.filter(status=1)
    return render(request,'table.html',{'data':li}) 

def edit_user(request,id):
    user=Register.objects.get(id=id)
    data={'title':'update | E_Luxuria','user':user}
    return render(request,'Edit.html',data)
def delete_user(request,id):
    user=Register.objects.get(id=id)
    
    user.status=0
    # user.delete()
    user.save=()
    return redirect('regis')
def retrive_user(request,id):
    user=Register.objects.get(id=id)
    #user.delete()
    user.status=1
    user.save()
    return redirect('regis')
def update(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        Password = request.POST['Password']
        Mobile_No = request.POST['Mobile_No']
        Address= request.POST['Address']
        Gender= request.POST['Gender']
        Country = request.POST['Country']
        State = request.POST['State']
        PIN = request.POST['PIN'] 
        id=request.POST['edit_id']
        user=Register.objects.get(id=id)
        user.email=email
        user.Password=Password
        user.Address=Address
        user.Mobile_No=Mobile_No
        user.Gender=Gender
        user.Country=Country
        user.State=State
        user.PIN=PIN
        user.name=name
        user.save()
    return redirect('regis') 

def Signout(request):
    del request.session['email']
    #messages.add_message(request,messages.SUCCESS,'Signout successful')
    return redirect('index')

def cart(request):
    if request.method=='POST':
        pid=request.POST['pid']
        uid=request.POST['uid']
        qty=request.POST['qty']
        Cart.objects.create(pid=pid,uid=uid,qty=qty,status=1)
        return redirect('cart')
    cart_items=Cart.objects.filter(status=1)
    data={'cart_items':cart_items}
    return render(request,'cart.html',data)

def product(request):
    product=Product.objects.filter(status=1)
    data={'product':product}
    
    return render(request,'product.html',data)

def checkout(request):
    return render(request,'checkout.html')

def mens(request):
    return render(request,'mens.html')

def womens(request):
    return render(request,'womens.html')

def Kids(request):
    return render(request,'Kids.html')

def detail(request):
    return render(request,'detail.html')

def contact(request):
    return render(request,'contact.html')

 