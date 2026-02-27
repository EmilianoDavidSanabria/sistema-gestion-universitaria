from django.contrib import admin
from .models import (
    Facultad,
    Departamento,
    Carrera,
    Profesor,
    Curso,
    Estudiante,
    Inscripcion,
    Examen,
    Aula
)

admin.site.register(Facultad)
admin.site.register(Departamento)
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Examen)
admin.site.register(Aula)
