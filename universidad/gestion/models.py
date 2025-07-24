from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    matricula = models.CharField(max_length=10, unique=True)
    carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE)
    semestre = models.IntegerField()
    promedio_calificaciones = models.FloatField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.matricula}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.especialidad}'


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_semestres = models.IntegerField()
    facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    creditos = models.IntegerField()
    
    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    calificacion_final = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.estudiante} inscrito en {self.curso}'


class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    decano = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre



class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre



class Examen(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f'Examen de {self.curso} el {self.fecha}'



class Aula(models.Model):
    numero = models.CharField(max_length=10)
    edificio = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f'Aula {self.numero} en {self.edificio}'
