from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre del producto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Arroz 1kg'})
    )
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del producto'})
    )
    precio = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Precio",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ej: 2.50'})
    )
    stock = forms.IntegerField(
        label="Stock",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 50'})
    )
    categoria = forms.ChoiceField(
        choices=[
            ('Alimentos', 'Alimentos'),
            ('Bebidas', 'Bebidas'),
            ('Limpieza', 'Limpieza'),
            ('Higiene', 'Higiene'),
            ('Lácteos', 'Lácteos'),
            ('Otros', 'Otros'),
        ],
        label="Categoría",
        widget=forms.Select(attrs={'class': 'form-control'})
    )