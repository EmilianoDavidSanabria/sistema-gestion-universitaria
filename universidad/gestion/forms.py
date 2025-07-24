from django import forms
from .models import Estudiante, Inscripcion, Profesor, Carrera, Curso, Examen, Facultad, Departamento, Aula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Importar el modelo User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'matricula', 'semestre', 'promedio_calificaciones', 'carrera', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
        
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad', 'departamento']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'facultad', 'duracion_semestres']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'carrera', 'profesor', 'creditos']

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['curso', 'fecha', 'descripcion']

class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = ['nombre']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'facultad']

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['numero', 'capacidad', 'edificio']  # Ajustado para coincidir con los campos del modelo Aula
