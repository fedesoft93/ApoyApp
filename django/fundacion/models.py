from django.db import models

class Entidad(models.Model): #VarChar
    nombre = models.CharField(
        max_length=200,
        verbose_name='Nombre',
        )
    identificacion = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        verbose_name='Número de Identificación',
        )
    
    def __str__(self):
        return self.nombre

class Fundacion(Entidad):
    direccion = models.CharField(
        max_length=20,
        )
    descripcion = models.CharField(
        max_length=255,
        blank=True, 
        null=True,
        )
    telefono = models.CharField(
        max_length=10,
        blank=True, 
        null=True,
        )
    ciudad = models.CharField(
        max_length=255,
        blank=True, 
        null=True,
        )
    hora_inicio = models. TimeField(
        verbose_name='Hora de Apertura',
    )
    hora_fin = models. TimeField(
        verbose_name='Hora de Cierre',
    )
    latitud = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
        )
    longitud = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
        )
    logo = models.ImageField(
        upload_to='img/fundacion/', 
        blank=True, 
        null=True,
        )

class Persona(Entidad): #Herencia: https://es.stackoverflow.com/questions/23910/herencia-en-modelos-de-django
    telefono = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    apellido = models.CharField(
        max_length=20
        )
    genero = models.CharField(
        max_length=1,
        choices=(
            ('m', 'masculino'),
            ('f', 'femenino'),
            ('i', 'indefinido'),
        ),
        default='m',
    )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True,
    )
    dir_correo = models.EmailField(
    )
    foto = models.ImageField(
        upload_to='img/persona/', 
        blank=True, 
        null=True,
        )
    fundacion_ids = models.ManyToManyField(
        Fundacion,
        null=True,
        blank=True,
        )

class Evento(models.Model):
    nombre = models.CharField(
        max_length=20
        )
    fundacion_ids = models.ForeignKey(
        Fundacion, 
        on_delete=models.CASCADE
        )
    imagen = models.ImageField(
        upload_to='img/persona/', 
        blank=True, 
        null=True,
        )
    fecha_hora_inicio = models. DateTimeField(
    )
    fecha_hora_fin = models. DateTimeField(
    )
    latitud = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
        )
    longitud = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
        )
    descripcion = models.TextField(
        )

    def __str__(self):
        return self.nombre

class Apoyo(models.Model):
    nombre = models.CharField(
        max_length=20
        )
    apellido = models.CharField(
        max_length=20
        )
    identificacion = models.CharField(
        max_length=20
        )    
    fundacion_ids =models.ForeignKey(
        Fundacion,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.nombre

class Apoyo_Voluntario(Apoyo):
    direccion = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    tel_fijo = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    tel_movil = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        )
    dir_correo = models.EmailField()
    situacion_laboral = models.CharField(
        max_length=1,
        choices=(
            ('e', 'empleado'),
            ('i', 'independiente'),
            ('d', 'desempleado'),
            ),
        default='e',
        )
    profesion = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        )
    empresa = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        )
    

class Apoyo_Monetario(Apoyo):
    valor_donacion = models.CharField(
        max_length=10
        )
    confirmacion = models.CharField(
        max_length=100
        )
    dir_correo = models.EmailField()

class Apoyo_Menaje(models.Model):
    tipo_donacion = models.CharField(
        max_length=1,
        choices=(
            ('a', 'alimento'),
            ('m', 'medicina'),
            ('e', 'enseres'),
            ),
        default='e',
        )
    descripcion = models.TextField(
        )
    activo = models.BooleanField()
    fundacion_ids =models.ForeignKey(
        Fundacion,
        on_delete=models.CASCADE
        )