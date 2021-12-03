from django.db import models

# Create your models here.


# Create your models here.
class Categorias(models.Model):
    idcategorias = models.AutoField(db_column='idCategorias', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.descripcion

class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.descripcion

class Zona(models.Model):
    idzona = models.AutoField(db_column='idZona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=80, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    idclientes = models.AutoField(primary_key=True)
    nombres = models.CharField(db_column='Nombres', max_length=45)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idcategorias = models.IntegerField(db_column='idCategorias', blank=True, null=True)  # Field name made lowercase.
    idzona = models.IntegerField(db_column='idZona', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idestado = models.IntegerField(db_column='idEstado', blank=True, null=True)  # Field name made lowercase.