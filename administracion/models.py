
from tabnanny import verbose
from django.db import models

# Create your models here.

class Emprendimiento(models.Model):

    TIPO = [
        ('hospedaje', 'Hospedaje'),
        ('restaurantes', 'Restaurante'),
        ('spots', 'Spot Turistico'),
        ('productores', 'Productor - Vendedor'),
    ]

    tipo_emprendimiento = models.CharField(verbose_name="Tipo de Emprendimiento", max_length=200, choices=TIPO)
    empresa = models.CharField(verbose_name="Nombre del Emprendimiento", max_length=200)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    decripcion = models.TextField()
    horario_apertura = models.DateTimeField()
    horario_cierre = models.DateTimeField()
    altitud = models.CharField(verbose_name="Altitud", max_length=20)
    latitud = models.CharField(verbose_name="Latitud", max_length=20)
    foto = models.ImageField(upload_to = "fotos_local", verbose_name = "Logo", null = True, blank = True)
    video = models.URLField(verbose_name="Video Promocional", null=True, blank=True)

    class Meta:
        verbose_name = "Emprendimiento"
        verbose_name_plural = "Emprendimientos"

    def __str__(self) -> str:
        return self.tipo_emprendimiento + self.empresa

class Producto(models.Model):
    nombre_producto = models.CharField(verbose_name="Nombre del Producto", max_length=100)
    descripcion_producto = models.TextField
    cantidad = models.IntegerField(verbose_name="Cantidad del Prodcuto", max_length=4)
    



class Persona(models.Model):

    TIPO_DOCUMENTO = [
        ('cedula','Cedula'),
        ('pasaporte','Pasaporte'),

    ]

    tipo_documento = models.CharField(verbose_name="Tipo de Documento", max_length=20, choices = TIPO_DOCUMENTO)
    num_documento = models.CharField(verbose_name="Número de Documento", max_length = 13)
    nombre = models.CharField(verbose_name="Nombre", max_length = 100)
    apellido = models.CharField(verbose_name="Apellido", max_length = 100)
    email = models.EmailField(verbose_name="E-mail")
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    direccion = models.CharField(verbose_name="Dirección", max_length=13)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    pais_origen = models.CharField(verbose_name="País de origen", max_length=200)
    foto = models.ImageField(upload_to = "fotos_usuarios", verbose_name = "Foto de Perfil", null = True, blank = True)



    # metodo para presentar el objeto creado
    def __str__(self):
        return self.cedula

    


class Cliente(Persona):

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Administrador(Persona):
    fecha_inicio = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    estado = models.BooleanField()

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Emprendedor(Persona):

    emprendimientos = models.ManyToManyField(Emprendimiento, blank=True, null=True)
    
    class Meta:
        verbose_name = "Emprendedor"
        verbose_name_plural = "Emprendedores"




