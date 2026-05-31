from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('About/',views.About,name='About'),
   path('Signin/',views.Signin,name='Signin'),
   path('Signout/',views.Signout,name='Signout'),
   path('Shop/',views.Shop,name='Shop'),
   path('signup/',views.Signup,name='Signup'),
   path('cart/',views.cart,name='cart'),
   path('checkout/',views.checkout,name='checkout'),
   path('product/',views.product,name='product'),
   path('regis/',views.regis,name='regis'),
   path('edit_user/<id>',views.edit_user,name='edit_user'),
   path('delete_user/<id>',views.delete_user,name='delete_user'),
   path('retrive_user/<id>',views.retrive_user,name='retrive_user'),
   path('update',views.update,name='update'),
   path('mens/',views.mens,name='mens'),
   path('womens/',views.womens,name='womens'),
   path('Kids/',views.Kids,name='Kids'),
   path('detail/',views.detail,name='detail'),
   path('contact/',views.contact,name='contact'),
]