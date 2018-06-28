from django.db import models
from django.db.models.deletion import DO_NOTHING
from _decimal import Decimal

# Create your models here.


class Licitacion(models.Model):
    nombre=models.CharField(max_length=150)
    publicada=models.BooleanField()
    def __str__(self):
        return str(self.id)+" - "+self.nombre
class Contrato(models.Model):
    nombre=models.CharField(max_length=150)
    fecha=models.DateField()
    
    def __str__(self):
        return str(self.id)+" - "+self.nombre
    #Relaciones
    licitacion=models.ForeignKey(Licitacion,related_name='contratos',on_delete=DO_NOTHING)

class Factura(models.Model):
    nombre=models.CharField(max_length=150)
    fecha=models.DateField(blank=True,null=True)
    adjunto=models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    
    precio=models.DecimalField(max_digits=12, decimal_places=2)
    
    #DERIVADOS
    @property
    def iva(self):
        return round(self.precio*Decimal(0.21),2)
    
    @property 
    def total(self):
        return round(Decimal(self.iva+self.precio),2)
    
    
    
    #RELACIONES
    contrato=models.ForeignKey(Contrato,related_name='Facturas', on_delete=DO_NOTHING,blank=True,null=True)
    licitacion=models.ForeignKey(Licitacion,related_name='FacturasA',on_delete=DO_NOTHING,blank=True,null=True)
