from django.test import TestCase
from .models import Facultad, Departamento, Carrera, Profesor, Curso, Estudiante, Inscripcion
from django.urls import reverse

class ModelTest(TestCase):

    def setUp(self):
        self.facultad = Facultad.objects.create(
            nombre="Ingeniería",
            decano="Dr. Pérez"
        )

        self.departamento = Departamento.objects.create(
            nombre="Computación",
            facultad=self.facultad
        )

        self.carrera = Carrera.objects.create(
            nombre="Ingeniería en Sistemas",
            duracion_semestres=10,
            facultad=self.facultad
        )

        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Gómez",
            especialidad="Algoritmos",
            departamento=self.departamento
        )

        self.curso = Curso.objects.create(
            nombre="Programación",
            codigo="PRG101",
            profesor=self.profesor,
            carrera=self.carrera,
            creditos=5
        )

        self.estudiante = Estudiante.objects.create(
            nombre="Ana",
            apellido="Lopez",
            fecha_nacimiento="2000-01-01",
            matricula="A123",
            carrera=self.carrera,
            semestre=3,
            promedio_calificaciones=8.5
        )

    def test_creacion_estudiante(self):
        self.assertEqual(self.estudiante.nombre, "Ana")

    def test_str_curso(self):
        self.assertEqual(str(self.curso), "Programación")

    def test_relacion_profesor_curso(self):
        self.assertEqual(self.curso.profesor.nombre, "Juan")


class ViewTest(TestCase):

    def setUp(self):
        self.facultad = Facultad.objects.create(
            nombre="Ingeniería",
            decano="Dr. Pérez"
        )

        self.carrera = Carrera.objects.create(
            nombre="Sistemas",
            duracion_semestres=10,
            facultad=self.facultad
        )

        self.estudiante = Estudiante.objects.create(
            nombre="Carlos",
            apellido="Ruiz",
            fecha_nacimiento="2001-01-01",
            matricula="B123",
            carrera=self.carrera,
            semestre=2,
            promedio_calificaciones=7.5
        )

    def test_inicio_view(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_listar_estudiantes(self):
        response = self.client.get(reverse('listar_estudiantes'))
        self.assertEqual(response.status_code, 200)

    def test_detalle_estudiante(self):
        response = self.client.get(
            reverse('detalle_estudiante', args=[self.estudiante.id])
        )
        self.assertEqual(response.status_code, 200)

class InscripcionTest(TestCase):

    def setUp(self):
        facultad = Facultad.objects.create(nombre="Ingeniería", decano="Dr. Pérez")

        departamento = Departamento.objects.create(
            nombre="Computación",
            facultad=facultad
        )

        carrera = Carrera.objects.create(
            nombre="Sistemas",
            duracion_semestres=10,
            facultad=facultad
        )

        profesor = Profesor.objects.create(
            nombre="Mario",
            apellido="Diaz",
            especialidad="Backend",
            departamento=departamento
        )

        self.curso = Curso.objects.create(
            nombre="Django",
            codigo="DJ101",
            profesor=profesor,
            carrera=carrera,
            creditos=5
        )

        self.estudiante = Estudiante.objects.create(
            nombre="Laura",
            apellido="Martinez",
            fecha_nacimiento="2000-05-05",
            matricula="C123",
            carrera=carrera,
            semestre=4,
            promedio_calificaciones=9
        )

    def test_crear_inscripcion(self):
        inscripcion = Inscripcion.objects.create(
            estudiante=self.estudiante,
            curso=self.curso
        )

        self.assertEqual(inscripcion.estudiante.nombre, "Laura")
        self.assertEqual(inscripcion.curso.nombre, "Django")

