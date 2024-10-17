from django.shortcuts import render
from .models import Nuevatabla



def IndexView(request):
    # Obtener todos los productos de la base de datos
    registros = Nuevatabla.objects.all()  # Traer todos los productos
    
    # Pasar los productos a la plantilla
    return render(request, "index.html", {'registros': registros})