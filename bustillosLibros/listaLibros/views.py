from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("bookList:ver-libro"))

def VerLibros(request):
    # Con order_by obtengo todos los elementos pero ordenados alfabeticamente con el título
    djangoModel = models.newBook.objects.order_by('tituloD')
    return render(request, "seeBooks.html", { "listaLibros": djangoModel})

def VerDetalles(request, bookTitle):
    try:
        bookModel = models.newBook.objects.get(tituloD = bookTitle)
        return render(request, "bookDetail.html", {"bookDetail": bookModel})

    except:
        return HttpResponse("Funciona")
        # return render(request, "404Contact.html", {"img": "../static/notFoundImages/404Contact.png"})