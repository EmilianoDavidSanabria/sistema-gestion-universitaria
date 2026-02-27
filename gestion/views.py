from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Aula, Departamento, Examen, Facultad, Inscripcion, Estudiante, Curso, Carrera, Profesor 
from .forms import EstudianteForm, InscripcionForm, ProfesorForm, CarreraForm, CursoForm, ExamenForm, FacultadForm, DepartamentoForm, AulaForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages

def inicio(request):
    # puede ser una plantilla simple para probar
    return render(request, 'inicio.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # loguea al usuario automáticamente
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('inicio')  # o donde quieras redirigir
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/listar_estudiantes.html', {'estudiantes': estudiantes})


def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    return render(request, 'estudiantes/detalle_estudiante.html', {'estudiante': estudiante})


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/crear_estudiante.html', {'form': form})


def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/editar_estudiante.html', {'form': form})


def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    estudiante.delete()
    return redirect('estudiantes/listar_estudiantes')


def buscar_estudiantes(request):
    query = request.GET.get('q')
    if query:
        estudiantes = Estudiante.objects.filter(nombre__icontains=query) | Estudiante.objects.filter(matricula__icontains=query)
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/buscar_estudiantes.html', {'estudiantes': estudiantes})


def filtrar_estudiantes(request):
    semestre = request.GET.get('semestre')
    promedio_min = request.GET.get('promedio_min')
    estudiantes = Estudiante.objects.all()
    if semestre:
        estudiantes = estudiantes.filter(semestre=semestre)
    if promedio_min:
        estudiantes = estudiantes.filter(promedio_calificaciones__gte=promedio_min)
    return render(request, 'estudiantes/listar_estudiantes.html', {'estudiantes': estudiantes})


def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/listar_profesores.html', {'profesores': profesores})


def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'profesores/detalle_profesor.html', {'profesor': profesor})


def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'profesores/crear_profesor.html', {'form': form})


def editar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesores/editar_profesor.html', {'form': form})


def eliminar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    profesor.delete()
    return redirect('listar_profesores')


def filtrar_profesores(request):
    departamento = request.GET.get('departamento')
    especialidad = request.GET.get('especialidad')
    profesores = Profesor.objects.all()
    if departamento:
        profesores = profesores.filter(departamento__nombre=departamento)
    if especialidad:
        profesores = profesores.filter(especialidad__icontains=especialidad)
    return render(request, 'profesores/listar_profesores.html', {'profesores': profesores})


def listar_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/listar_carreras.html', {'carreras': carreras})


def detalle_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, id=carrera_id)
    return render(request, 'carreras/detalle_carrera.html', {'carrera': carrera})


def crear_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carreras')
    else:
        form = CarreraForm()
    return render(request, 'carreras/crear_carrera.html', {'form': form})


def editar_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, id=carrera_id)
    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('listar_carreras')
    else:
        form = CarreraForm(instance=carrera)
    return render(request, 'carreras/editar_carrera.html', {'form': form})


def eliminar_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, id=carrera_id)
    carrera.delete()
    return redirect('listar_carreras')


def filtrar_carreras(request):
    facultad = request.GET.get('facultad')
    carreras = Carrera.objects.all()
    if facultad:
        carreras = carreras.filter(facultad__nombre=facultad)
    return render(request, 'carreras/listar_carreras.html', {'carreras': carreras})


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})


def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})


def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('cursos/listar_cursos')



def filtrar_cursos(request):
    carrera = request.GET.get('carrera')
    profesor = request.GET.get('profesor')
    cursos = Curso.objects.all()
    if carrera:
        cursos = cursos.filter(carrera__nombre=carrera)
    if profesor:
        cursos = cursos.filter(profesor__nombre=profesor)
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})


def inscribir_estudiante(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirijo al reporte de inscripciones por semestre
            return redirect('reporte_inscripciones_por_semestre')
    else:
        form = InscripcionForm()
    return render(request, 'inscripciones/inscribir_estudiante.html', {'form': form})



def inscripciones_por_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante)
    return render(request, 'inscripciones/inscripciones_por_estudiante.html', {'estudiante': estudiante, 'inscripciones': inscripciones})


def estudiantes_inscritos_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    inscripciones = Inscripcion.objects.filter(curso=curso)
    estudiantes = [inscripcion.estudiante for inscripcion in inscripciones]
    return render(request, 'inscripciones/estudiantes_inscritos_curso.html', {'curso': curso, 'estudiantes': estudiantes})


def eliminar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    inscripcion.delete()
    return redirect('listar_inscripciones')


def listar_examenes(request):
    examenes = Examen.objects.all()
    return render(request, 'examenes/listar_examenes.html', {'examenes': examenes})


def detalle_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    return render(request, 'examenes/detalle_examen.html', {'examen': examen})


def crear_examen(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_examenes')
    else:
        form = ExamenForm()
    return render(request, 'examenes/crear_examen.html', {'form': form})


def editar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    if request.method == 'POST':
        form = ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect('listar_examenes')
    else:
        form = ExamenForm(instance=examen)
    return render(request, 'examenes/editar_examen.html', {'form': form})


def eliminar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    examen.delete()
    return redirect('examenes/listar_examenes')


def filtrar_examenes(request):
    curso = request.GET.get('curso')
    fecha = request.GET.get('fecha')
    examenes = Examen.objects.all()
    if curso:
        examenes = examenes.filter(curso__nombre=curso)
    if fecha:
        examenes = examenes.filter(fecha=fecha)
    return render(request, 'examenes/listar_examenes.html', {'examenes': examenes})


def listar_facultades(request):
    facultades = Facultad.objects.all()
    return render(request, 'facultades/listar_facultades.html', {'facultades': facultades})


def detalle_facultad(request, facultad_id):
    facultad = get_object_or_404(Facultad, id=facultad_id)
    return render(request, 'facultades/detalle_facultad.html', {'facultad': facultad})


def crear_facultad(request):
    if request.method == 'POST':
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facultades')
    else:
        form = FacultadForm()
    return render(request, 'facultades/crear_facultad.html', {'form': form})


def editar_facultad(request, facultad_id):
    facultad = get_object_or_404(Facultad, id=facultad_id)
    if request.method == 'POST':
        form = FacultadForm(request.POST, instance=facultad)
        if form.is_valid():
            form.save()
            return redirect('listar_facultades')
    else:
        form = FacultadForm(instance=facultad)
    return render(request, 'facultades/editar_facultad.html', {'form': form})



def eliminar_facultad(request, facultad_id):
    facultad = get_object_or_404(Facultad, id=facultad_id)
    facultad.delete()
    return redirect('listar_facultades')


def departamentos_y_carreras_facultad(request, facultad_id):
    facultad = get_object_or_404(Facultad, id=facultad_id)
    departamentos = Departamento.objects.filter(facultad=facultad)
    carreras = Carrera.objects.filter(facultad=facultad)
    return render(request, 'departamentos/departamentos_y_carreras.html', {'facultad': facultad, 'departamentos': departamentos, 'carreras': carreras})


def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/listar_departamentos.html', {'departamentos': departamentos})


def detalle_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    return render(request, 'departamentos/detalle_departamento.html', {'departamento': departamento})


def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'departamentos/crear_departamento.html', {'form': form})


def editar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamentos/editar_departamento.html', {'form': form})


def eliminar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    departamento.delete()
    return redirect('listar_departamentos')


def filtrar_departamentos(request):
    facultad = request.GET.get('facultad')
    departamentos = Departamento.objects.all()
    if facultad:
        departamentos = departamentos.filter(facultad__nombre=facultad)
    return render(request, 'departamentos/listar_departamentos.html', {'departamentos': departamentos})


def profesores_por_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    profesores = Profesor.objects.filter(departamento=departamento)
    return render(request, 'departamentos/profesores_por_departamento.html', {'departamento': departamento, 'profesores': profesores})


def listar_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/listar_aulas.html', {'aulas': aulas})


def detalle_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    return render(request, 'aulas/detalle_aula.html', {'aula': aula})


def crear_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulaForm()
    return render(request, 'aulas/crear_aula.html', {'form': form})


def editar_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulaForm(instance=aula)
    return render(request, 'aulas/editar_aula.html', {'form': form})


def eliminar_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    aula.delete()
    return redirect('listar_aulas')


def filtrar_aulas(request):
    capacidad = request.GET.get('capacidad')
    edificio = request.GET.get('edificio')
    aulas = Aula.objects.all()
    if capacidad:
        aulas = aulas.filter(capacidad__gte=capacidad)
    if edificio:
        aulas = aulas.filter(edificio=edificio)
    return render(request, 'aulas/listar_aulas.html', {'aulas': aulas})


def reporte_estudiantes(request):
    carrera = request.GET.get('carrera')
    semestre = request.GET.get('semestre')
    promedio = request.GET.get('promedio')
    
    estudiantes = Estudiante.objects.all()
    if carrera:
        estudiantes = estudiantes.filter(carrera__nombre=carrera)
    if semestre:
        estudiantes = estudiantes.filter(semestre=semestre)
    if promedio:
        estudiantes = estudiantes.filter(promedio_calificaciones__gte=promedio)
    
    return render(request, 'reportes/reporte_estudiantes.html', {'estudiantes': estudiantes})


def reporte_estudiantes_por_curso(request):
    cursos = Curso.objects.all()
    reportes = []
    for curso in cursos:
        total_estudiantes = Inscripcion.objects.filter(curso=curso).count()
        reportes.append({'curso': curso, 'total_estudiantes': total_estudiantes})
    return render(request, 'reportes/reporte_estudiantes_por_curso.html', {'reportes': reportes})


def cursos_por_profesor(request):
    profesores = Profesor.objects.all()
    reportes = []
    for profesor in profesores:
        total_cursos = Curso.objects.filter(profesor=profesor).count()
        reportes.append({'profesor': profesor, 'total_cursos': total_cursos})
    return render(request, 'reportes/cursos_por_profesor.html', {'reportes': reportes})


def reporte_inscripciones_por_semestre(request):
    semestre = request.GET.get('semestre')
    inscripciones = Inscripcion.objects.filter(estudiante__semestre=semestre)
    return render(request, 'reportes/reporte_inscripciones_por_semestre.html', {'inscripciones': inscripciones})

