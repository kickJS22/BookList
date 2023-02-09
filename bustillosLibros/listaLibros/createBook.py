from . import models
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class newBookForm(forms.Form):
    # Con widget=forms.TextInput(attrs={'autofocus': True}) lo que le digo es que me agregue un atributo/widget de autofocus
    tituloF = forms.CharField(label="Título", widget=forms.TextInput(attrs={'autofocus': True}))
    autorF = forms.CharField(label="Autor")
    yearF = forms.IntegerField(label="Año de publicación")
    cantPagF = forms.IntegerField(label="Cantidad de Págs.")
    precioF = forms.IntegerField(label="Precio")


def newBook(request):

    if request.method == "POST":

        sendedForm = newBookForm(request.POST)

        if sendedForm.is_valid():

            newTitle = sendedForm.cleaned_data["tituloF"]
            # .title() sirve para convertir a mayuscula la primera letra de cada palabra 
            newTitle = newTitle.title()
            newAutor = sendedForm.cleaned_data["autorF"]
            newAutor = newAutor.title()
            newYear = sendedForm.cleaned_data["yearF"]
            newCantPage = sendedForm.cleaned_data["cantPagF"]
            newPrice = sendedForm.cleaned_data["precioF"]

            toDataBase(newTitle, newAutor, newYear, newCantPage, newPrice)

            return HttpResponseRedirect(reverse("bookList:ver-libro"))

        else:  
           return render(request, "createBook.html", { "djangoForm":newBookForm })

    else:
         return render(request, "createBook.html", { "djangoForm":newBookForm })



def toDataBase (titulo, autor, year, cantPag, precio):

    book = models.newBook(tituloD = titulo, autorD = autor, yearD = year, cantPagD = cantPag, precioD = precio)

    book.save()