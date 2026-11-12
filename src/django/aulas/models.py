from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre=models.CharField(max_length=128)

class Profesor(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=128)
    mostrar=models.CharField(max_length=256)

class Materia(models.Model):
    nombre=models.CharField(max_length=128)
    cant_alumnos=models.IntegerField(default=5)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    profesor=models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Aula(models.Model):
    descripcion=models.CharField(max_length=128)
    ubicacion=models.CharField(max_length=128)
    cant_proyector=models.IntegerField(default=0)
    aforo=models.IntegerField(default=0)
    es_climatizada=models.BooleanField(default=False)

'''
id autoincrementales: no los agregué porque Django los genera por defecto.
null: por defecto está en false, solo se registra cuando una columna tiene que ser null cambiandolo a true.
FK: siempre on_delete=models.CASCADE para borrar el registro relacionado(ej:materia) al objeto padre(ej:Carrera) por así decirlo.
id de FK: tampoco hace falta porque Django ya asigna ej: carrera_id por defecto
'''
