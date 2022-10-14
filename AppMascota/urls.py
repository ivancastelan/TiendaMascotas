from .views import *
from django.urls import path, include
from . import views



urlpatterns = [

    path('', inicio, name="Home"),

    path("login", inicioSesion, name="Login"),
    path("register", registroUser, name="Registro"),


    #CRUD Articulo

    path("articulo/list/", ListaArticulo.as_view(), name="ArticuloLeer"),
    path("articulo/<int:pk>", DetalleArticulo.as_view(), name="ArticuloDetalle"),
    path("articulo/crear/", CrearArticulo.as_view(), name="ArticuloCrear"),
    path("articulo/editar/<int:pk>", EditarArticulo.as_view(), name="ArticuloEditar"),
    path("articulo/borrar/<int:pk>", BorrarArticulo.as_view(), name="ArticuloBorrar"),

    path('pricing/', views.about, name='pricing')


]

