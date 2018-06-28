from django.shortcuts import render, get_object_or_404, redirect
from frontend.models import Factura, Contrato, Licitacion
from frontend.forms import FacturaForm
import time
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
@login_required(login_url='/login/')
def facturas(request):
    facturas=Factura.objects.all()
    
    return render(request,'facturas.html',{'facturas':facturas})
@login_required(login_url='/login/')
def newFactura(request):
    
   
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        
        if form.is_valid():
            
            
            factura = form.save(commit=False)
            factura.fecha=time.strftime("%Y-%m-%d")
            factura = form.save()
           
            return redirect('facturas')  
    else:
        factura=Factura()
        factura.fecha=time.strftime("%Y-%m-%d")
        form = FacturaForm(instance=factura)
   
    return render(request, 'factura.html', { 'form': form,'idF':str(0)})
@login_required(login_url='/login/')
def editFactura(request,pk):
    factura=get_object_or_404(Factura,pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, request.FILES, instance=factura)
        
        if form.is_valid():
            factura = form.save()
            
    #else:
        
        
    form=FacturaForm(instance=factura)
    
    
    return render(request,'factura.html',{'form':form,'idF':str(factura.id),
                                          'iva':factura.iva,"total":factura.total})
@login_required(login_url='/login/')
def deleteFactura(request,pk):
    factura=get_object_or_404(Factura,pk=pk)
    factura.delete()
    
    return redirect('facturas') 
 
@login_required(login_url='/login/')
def loadContratos(request):
    licitacion_id = request.GET.get('licitacion')
    contratos = Contrato.objects.filter(licitacion_id=licitacion_id).order_by('nombre')
    return render(request, 'hr/contrato_dropdown_list_options.html', {'contratos': contratos})


class LicitacionesList(ListView):
    model=Licitacion
    template_name='licitacion_list.html'

class LicitacionCreate(CreateView):
    model=Licitacion
    fields=['nombre','publicada']
    template_name='frontend/edit_template.html' 
     
    
class LicitacionUpdate(UpdateView):
    model=Licitacion
    fields=['nombre','publicada']
    template_name='frontend/edit_template.html' 
    
def LicitacionDelete(request,pk):
    licitacion=get_object_or_404(Licitacion,pk=pk)
    licitacion.delete()
    
    return redirect('licitaciones') 

def ContratoList(request):
    contratos=Contrato.objects.all()
    
    return render(request,'frontend/contrato_list.html',{'contratos':contratos})

class ContratoCreate(CreateView):
    model=Contrato
    fields=['nombre','fecha','licitacion']
    template_name='frontend/edit_template.html' 
     
    
class ContratoUpdate(UpdateView):
    model=Contrato
    fields=['id','nombre','fecha','licitacion']
    template_name='frontend/edit_template.html' 
    
def ContratoDelete(request,pk):
    contrato=get_object_or_404(Contrato,pk=pk)
    contrato.delete()
    
    return redirect('contratos') 