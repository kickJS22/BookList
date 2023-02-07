from django.db import models

# Create your models here.
class newBook(models.Model):
    tituloD = models.CharField(max_length=80)
    autorD = models.CharField(max_length=80)
    yearD = models.IntegerField()
    cantPagD = models.IntegerField()
    precioD = models.IntegerField()
