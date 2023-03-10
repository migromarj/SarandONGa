from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils.text import slugify

SEX_TYPES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB', 'Tarjeta Bancaria'),
    ('E', 'Efectivo'),
)

STATUS = (
    ('C', 'Casado/a'),
    ('F', 'Fallecido/a'),
    ('V', 'Viudo/a'),
    ('S', 'Soltero/a'),
    ('D', 'Divorciado/a'),
)

FREQUENCY = (
    ('A', 'Anual'),
    ('M', 'Mensual'),
    ('T', 'Trimestral'),
    ('S', 'Semestral'),
)

CONDITION = (
    ('EM', 'Escleorosis múltiple'),
    ('ICTUS', 'Ictus'),
    ('ELA', 'Esclerosis lateral amiotrófica'),
    ('OTROS', 'Otros')
)

MEMBER = (
    ('EM', 'Escleorosis múltiple'),
    ('ICTUS', 'Ictus'),
    ('ELA', 'Esclerosis lateral amiotrófica'),
    ('OTROS', 'Otros'),
    ('UNA', 'Usuario no asociado')
)

USER_TYPE = (
    ('SCC', 'Socios ASEM con cuota de socio'),
    ('UCC', 'Usuarios con cuota de socio'),
    ('UCS', 'Usuarios sin cuota de socio')
)

CORRESPONDENCE = (
    ('E', 'Email'),
    ('CC', 'Carta con logo'),
    ('CS', 'Carta sin logo'),
    ('SR', 'Solo revista'),
    ('N', 'Ninguna')
)

HOUSING_TYPE = (
    ('VC', 'Vivienda compartida'),
    ('VP', 'Vivienda propia')
)


class Person(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surnames = models.CharField(max_length=200, verbose_name="Apellidos")
    email = models.CharField(max_length=200, verbose_name="Correo electrónico")
    birth_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de nacimiento")
    sex = models.CharField(
        max_length=50, choices=SEX_TYPES, verbose_name="Género")
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    telephone = models.IntegerField(verbose_name="Teléfono")
    postal_code = models.IntegerField(verbose_name="Código postal")

    # Extiende a clase WorkerProfile si es un trabajador
    is_worker = models.BooleanField(
        default=False, verbose_name="¿Es trabajador?")

    class Meta:
        abstract = True


class GodFather(Person):
    dni = models.CharField(max_length=9, unique=True,verbose_name='DNI')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD,verbose_name='Método de pago',)
    bank_account_number = models.CharField(max_length=24,verbose_name='Número de cuenta bancaria', validators=[RegexValidator(regex=r'^ES\d{2}\s?\d{4}\s?\d{4}\s?\d{1}\d{1}\d{10}$',message='El número de cuenta no es válido.')])
    bank_account_holder = models.CharField(max_length=100,verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(max_length=100,verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad',validators=[MinValueValidator(1)])
    frequency = models.CharField(max_length=20, choices=FREQUENCY,verbose_name='Frecuencia de pago')
    seniority = models.DateField(verbose_name='Antigüedad')
    notes = models.TextField(blank=True,verbose_name='Observaciones')
    status = models.CharField(max_length=20, choices=STATUS,verbose_name='Estado')
    slug = models.SlugField(max_length=200,unique=True, editable=False)
    #T0D0
    #Añadir relacion uno a muchos con entidad pago
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + ' ' + self.surnames)
        super(GodFather, self).save(*args, **kwargs)
        
         
    class Meta:
        ordering = ['name']
        verbose_name = 'Padrino'
        verbose_name_plural = 'Padrinos'

#class WorkerProfile(models.Model):
    #Person = models.OneToOneField(Person, on_delete=models.CASCADE)
    #ONG = models.OneToOneField(ONG, on_delete=models.CASCADE) #ONG en la que trabaja
    #active = models.BooleanField(default=True) #¿Sigue trabajando en la ONG?

class ASEMUser(Person):
    condition = models.CharField(
        max_length=20, choices=CONDITION, verbose_name='Condición médica')
    member = models.CharField(
        max_length=20, choices=MEMBER, verbose_name='Socio')
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE, verbose_name='Tipo de usuario')
    correspondence = models.CharField(
        max_length=20, choices=CORRESPONDENCE, verbose_name='Tipo de correspondencia')
    status = models.CharField(
        max_length=20, choices=STATUS, verbose_name='Estado')
    family_unit_size = models.IntegerField(
        verbose_name='Tamaño de la unidad familiar', validators=[MaxValueValidator(30)])
    own_home = models.CharField(
        max_length=20, choices=HOUSING_TYPE, verbose_name='Tipo de vivienda')
    own_vehicle = models.BooleanField(
        default=False, verbose_name='¿Tiene vehículo propio?')
    bank_account_number = models.CharField(max_length=24, verbose_name='Número de cuenta bancaria', validators=[
                                           RegexValidator(r'^[A-Z]{2}\d{22}$')])


