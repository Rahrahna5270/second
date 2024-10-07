# from django.urls import path
# from.import views

# urlpatterns = [
#     path('',views.home),
#     path('category/',views.Category),
#     path('product/',views.Product),
#     path('product<int:id>',views.prod,name='prodscat'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),  
    path('category', views.category_view),  
    path('product', views.product_view,name='product'),  
    path('product/<int:id>/', views.prod, name='prodscat'),
    path('view/<int:id>/', views.product_detail, name='viewprods'), 
    path('addcart/<int:id>/', views.addcart,name='addcart'),
    path('cart', views.cartpage, name='cartproduct'),
    path('wish', views.wishpage, name='wish'),
    path('wishlist/<int:id>/', views.wishlist,name='wishlist'),
    path('signup', views.signup,name='sign'),
    path('login', views.loginpage,name='loginpage'),
    path('logout', views.logoutpage,name='logout'),  
    path('remove/<int:id>/', views.remove,name='remove'),
    path('order',views.place_order,name='order'),
    path('confirm',views.order_confirmation,name='confirm'),
    path('createcat',views.create_category,name='createcat'),
    path('createpro',views.create_product,name='createpro'),
    path('createdproduct',views.createdprodct,name='createdp'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('adminpage',views.admin,name='adminpage'),






    
   

]
