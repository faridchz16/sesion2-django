from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PRODUCTOS, Producto, get_next_id, add_producto
from .forms import ProductoForm


def producto_list(request):
    return render(request, 'store/producto_list.html', {'productos': PRODUCTOS})


def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = Producto(
                id=get_next_id(),
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=float(form.cleaned_data['precio']),
                stock=form.cleaned_data['stock'],
                categoria=form.cleaned_data['categoria'],
            )
            add_producto(nuevo_producto)
            messages.success(request, f'Producto "{nuevo_producto.nombre}" agregado correctamente.')
            return redirect('producto_list')
    else:
        form = ProductoForm()

    return render(request, 'store/producto_form.html', {'form': form})