from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

#Home/Inicio

def inicio(request):

    return render(request, 'inicio.html')

#Login y Logout

def inicioSesion(request):

    if request.method =="POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)
                return render(request, "AppMascota/inicio.html", f"Bienvenido {user}")
        
        else:

            return render(request, "AppMascota/inicio.html", f"Los datos son incorrectos.")

    else:

        form = AuthenticationForm()
    
    return render(request, "AppMascota/login.html", {"formulario":form})


#Articulos CRUD

class ListaArticulo(ListView):

    model = Articulo
    template_name = "articulo_list.html"


class DetalleArticulo(DetailView):

    model = Articulo
    template_name = "articulo_detail.html"


class CrearArticulo(CreateView):

    model = Articulo
    success_url = "/AppMascota/articulo/list/"
    template_name = "articulo_form.html"
    fields = "__all__"
    

class EditarArticulo(UpdateView):

    model= Articulo
    success_url = "/AppMascota/articulo/list/"
    template_name = "articulo_detail.html"
    fields = "__all__"


class BorrarArticulo(DeleteView):

    model= Articulo
    success_url = "/AppMascota/articulo/list"
    template_name = "articulo_confirm_delete.html"
