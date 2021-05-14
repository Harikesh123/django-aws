"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from TEST import views
from IT.views import test, register

urlpatterns = [
                  # path('',views.index), #Index page
                  path('admin/', admin.site.urls),  # Admin panel
                  path('about/', views.about, name='about'),  # About page
                  path('blog/', views.blog, name='blog'),  # Blog Page
                  path('blogdetail/', views.blogdetail, name='blogdetail'),  # Blog Detail Page
                  path('bloggrid/', views.bloggrid, name='bloggrid'),  # Blog Grid
                  path('career/', views.career, name='career'),  # Career
                  path('cart/', views.cart, name='cart'),  # Cart
                  path('checkout/', views.checkout, name='checkout'),  # Checkout
                  path('repair/', views.computerrepair, name='computerrepair'),  # Repair
                  path('homedark/', views.homedark, name='homedark'),
                  path('register/', register, name='register'),
                  path('', test, name='services'),
                  # path('delete',delete,name='delete')
                  # path('delete/<int::id>', delete, name='delete')
                  # path('appointment/',views.makeappointment,name='makeappointment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
