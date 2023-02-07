from django.urls import URLPattern, path
from . import createBook
from . import views

app_name = "bookList"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-libro", createBook.newBook, name="crear-libro"),
    path("ver-libro", views.VerLibros, name="ver-libro"),
    path("ver-libro/<str:bookTitle>", views.VerDetalles, name="ver-detalles")
]