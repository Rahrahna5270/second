    
from django.shortcuts import   redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
 

# Home view
def home(request):
    products = product.objects.all()
    categories = category.objects.all()
    
    context = {
        'product': products,
        'category': categories,
    }
    return render(request, 'home.html', context)
# Category view

def category_view(request):
    categories = category.objects.all()
    return render(request, 'category.html', {'category': categories})

# Product view
def product_view(request):
    products = product.objects.all()
    return render(request, 'products.html', {'product': products})

# Filtered products by category view
def prod(request, id):
    products = product.objects.filter(Category__id=id)
    return render(request, 'prod.html', {'prod': products})
def product_detail(request,id):
    products=product.objects.get(id=id)
    return render(request, 'view_product.html', {'viewprods': products})
def admin(request):
    return render(request, 'admin.html')


def signup(request):

    if request.method=='POST':
        
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        # print(email,password)
        user=User.objects.create_user(username,email,password) 
        user.save()
    return render(request,'signup.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:

                return redirect('adminpage')
            else:
                return redirect('home')
        else:
            messages.error(request,'invalid credential')
            return redirect('loginpage')
    return render(request,'login.html')        
def logoutpage(request):
    logout(request)
    return redirect('home')
def addcart(request,id):
    if request.user.is_authenticated:
        user=request.user
        products=product.objects.get(id=id)
        cart_item=Cart.objects.filter(user=user,product=products).first()
        if cart_item:
            cart_item.quantity+=1
            cart_item.save()
            # messages.error(request,'Item already exist in cart')
            # cart_item.save()
            return redirect('product')
        else:
            Cart.objects.create(user=user,product=products,quantity=1)
            return redirect('cartproduct')

        # cartitem ,item_created=Cartitem.objects.get_or_create(cart=items,product=products)
        # if id in items:
        #     items.quantity+=1
        #     items.save()
        # totals=(items.quantity * items.rate) 
        # print(totals)
        # return render(request, 'cart.html',{'itemprice':itemprice})
        
    else:
        return redirect('loginpage') 
def cartpage(request):
    if request.user.is_authenticated:
        cartitems = Cart.objects.filter(user=request.user)
       
        totalprice=sum(item.quantity * item.product.rate for item in cartitems)
        # print(totalprice)
        both={
            'productsincart': cartitems,
            'total':totalprice,
        }
        return render(request, 'cart.html',both)
    else:
        return redirect('loginpage' )
def wishlist(request,id):
    if request.user.is_authenticated:
        user=request.user
        products=product.objects.get(id=id)
        wishlist=Wishlist.objects.filter(user=user,product=products).first()
        if wishlist:
    
            wishlist.save()
            # messages.error(request,'Item already exist in cart')
            # cart_item.save()
            return redirect('product')
        else:
            Wishlist.objects.create(user=user,product=products)
            return redirect('wishlist')
    else:
        return redirect('loginpage') 
def wishpage(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
       
        
        # print(totalprice)
        
        return render(request, 'wishlist.html',{'wishlist':wishlist})
    else:
        return redirect('loginpage' )

def remove(request, id):
    if request.user.is_authenticated:
        cartitem = Cart.objects.get(id=id, user=request.user)
        cartitem.delete()
        return redirect('cartproduct')
    else:
        return redirect('loginpage')

def place_order(request):
    cartitems=Cart.objects.filter(user=request.user)
    if not cartitems.exists():
        return redirect('product')
    
    exist_order=Order.objects.filter(user=request.user).first()
    if request.method=='POST':
        address=request.POST['address']
        if exist_order:
            exist_order.address=address
            exist_order.save()
        else:
            orders=Order.objects.create(user=request.user,address=address)
        cartitems.delete()
        return redirect('confirm')
    return render(request,'place_order.html',{'cartitems':cartitems,'user':request.user,'exist_address':exist_order.address if exist_order else ''})
 
def order_confirmation(request):
    return render(request,'order_confirmation.html')
def create_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CategoryForm()
    return render (request,'categoryform.html',{'form':form})    
def create_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form=ProductForm()
    return render (request,'productform.html',{'form':form})    

def createdprodct(request):
    products = product.objects.all()
    categories = category.objects.all()
    context = {
        'product': products,
        'category': categories,
    }
    return render(request,'createproduct.html',context)
def delete(request,id):
    products = product.objects.get(id=id)
    products.delete()
    return redirect('createdp')
def edit(request,id):
    edit=product.objects.get(id=id)
    form=ProductForm(request.POST,request.FILES)
    if request.method=='POST':
        if 'image' in request.FILES:
            image=request.FILES['image']
    
        name=request.POST.get('name')
        rate=request.POST.get('rate')
        
        Category=request.POST.get('Category')
        description=request.POST.get('description')
        if edit:
            edit.name=name 
            edit.rate=rate
            edit.Category
            edit.image=image
            edit.description
            edit.save()
        return redirect('createdp')
    else:
        form=ProductForm()

    return render(request,'edit.html',{'form':form})    
