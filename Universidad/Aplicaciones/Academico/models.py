from django.db import models

# Create your models here.

# es una clase que atrces de un orm object relational mapping, que tiene los frameworks que nos permite interacttuar con la bd

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        return ('El nombre del curso es ' + self.nombre +', con una cantidad de creditos de ' + str(self.creditos))