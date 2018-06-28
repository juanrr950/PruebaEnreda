"""PruebaEnreda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
from frontend.views import  LicitacionesList, ContratoList, ContratoCreate,\
    ContratoUpdate, ContratoDelete, LicitacionCreate, LicitacionUpdate
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.facturas, name='home'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}),
    
    path('admin/', admin.site.urls),
    path('facturas/', views.facturas,name='facturas'),
    path('facturas/new', views.newFactura,name='nuevaFactura'),
    path('facturas/edit/<int:pk>', views.editFactura,name='editarFactura'),
    path('facturas/delete/<int:pk>', views.deleteFactura,name='deleteFactura'),
    path('ajax/load-contratos/', views.loadContratos, name='ajax_load_contratos'),
    
    path('licitaciones/',login_required(LicitacionesList.as_view(),'login','/login/'),name='licitaciones'),
    path('licitaciones/new',login_required(LicitacionCreate.as_view(success_url="/licitaciones/"),'login','/login/')),
    path('licitaciones/edit/<int:pk>',login_required(LicitacionUpdate.as_view(success_url="/licitaciones/"),'login','/login/')),
    path('licitaciones/delete/<int:pk>',login_required(views.LicitacionDelete,'login','/login/')),
    
    path('contratos/',login_required(views.ContratoList,'login','/login/'),name='contratos'),
    path('contratos/new',login_required(ContratoCreate.as_view(success_url="/contratos/"),'login','/login/')),
    path('contratos/edit/<int:pk>',login_required(ContratoUpdate.as_view(success_url="/contratos/"),'login','/login/')),
    path('contratos/delete/<int:pk>',login_required(views.ContratoDelete,'login','/login/'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)