from django.contrib import admin
from frontend.models import Factura, Contrato, Licitacion

# Register your models here.
admin.site.register(Factura)
admin.site.register(Licitacion)
admin.site.register(Contrato)