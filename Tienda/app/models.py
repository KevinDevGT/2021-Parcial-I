from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    fecha_ingreso = models.DateTimeField()
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}, precio {self.precio}, cantidad {self.cantidad}, categoría {self.categoria}, marca {self.marca}'