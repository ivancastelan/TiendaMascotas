from django import forms


class FormularioArticulos(forms.Form):

    nombre = forms.CharField()
    animal = forms.CharField()
    categoria = forms.CharField()
    precio = forms.IntegerField()
    fecha = forms.DateField()


class FormularioReview(forms.Form):

    comentario = forms.CharField()
    usuario = forms.CharField()


#class Formulario