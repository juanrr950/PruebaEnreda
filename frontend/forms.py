#-*- coding: utf-8 -*-
from django import forms
from frontend.models import Factura


class FacturaForm(forms.ModelForm):
    fecha=forms.DateField(disabled=True,required=False)
    class Meta:
        model = Factura
        fields = ['id','nombre','fecha','adjunto','precio','licitacion','contrato']
        
        