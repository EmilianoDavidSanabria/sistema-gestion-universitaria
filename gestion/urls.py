from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API juego.",
        default_version='v1',

        description="""API para un sistema de gestión de un juego multijugador con funcionalidades avanzadas. 
        Permite la administración de jugadores, partidas en tiempo real, economía virtual y análisis de estadísticas. 
        Incluye autenticación JWT, emparejamiento dinámico y soporte para WebSocket.
        Diseñada para escalabilidad y seguridad, ideal para experiencias multijugador competitivas.""",
        
        terms_of_service="https://www.tusitio.com/policies/terms/",
        contact=openapi.Contact(email="contact@tusitio.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('register/', views.register, name='register'),
    
    #Autenticacion con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #1-
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #2- Autenticacion con JWT
    
    # Documentación con Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Vistas principales
    path('', views.inicio, name='inicio'),

    # Estudiantes
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:estudiante_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('estudiantes/buscar/', views.buscar_estudiantes, name='buscar_estudiantes'),
    path('estudiantes/filtrar/', views.filtrar_estudiantes, name='filtrar_estudiantes'),

    # Profesores
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('profesores/<int:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
    path('profesores/crear/', views.crear_profesor, name='crear_profesor'),
    path('profesores/editar/<int:profesor_id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:profesor_id>/', views.eliminar_profesor, name='eliminar_profesor'),
    path('profesores/filtrar/', views.filtrar_profesores, name='filtrar_profesores'),

    # Carreras
    path('carreras/', views.listar_carreras, name='listar_carreras'),
    path('carreras/<int:carrera_id>/', views.detalle_carrera, name='detalle_carrera'),
    path('carreras/crear/', views.crear_carrera, name='crear_carrera'),
    path('carreras/editar/<int:carrera_id>/', views.editar_carrera, name='editar_carrera'),
    path('carreras/eliminar/<int:carrera_id>/', views.eliminar_carrera, name='eliminar_carrera'),
    path('carreras/filtrar/', views.filtrar_carreras, name='filtrar_carreras'),

    # Cursos
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/filtrar/', views.filtrar_cursos, name='filtrar_cursos'),

    # Inscripciones
    path('inscripciones/crear/', views.inscribir_estudiante, name='inscribir_estudiante'),
    path('inscripciones/estudiante/<int:estudiante_id>/', views.inscripciones_por_estudiante, name='inscripciones_por_estudiante'),
    path('inscripciones/curso/<int:curso_id>/', views.estudiantes_inscritos_curso, name='estudiantes_inscritos_curso'),
    path('inscripciones/eliminar/<int:inscripcion_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),

    # Exámenes
    path('examenes/', views.listar_examenes, name='listar_examenes'),
    path('examenes/<int:examen_id>/', views.detalle_examen, name='detalle_examen'),
    path('examenes/crear/', views.crear_examen, name='crear_examen'),
    path('examenes/editar/<int:examen_id>/', views.editar_examen, name='editar_examen'),
    path('examenes/eliminar/<int:examen_id>/', views.eliminar_examen, name='eliminar_examen'),
    path('examenes/filtrar/', views.filtrar_examenes, name='filtrar_examenes'),

    # Facultades
    path('facultades/', views.listar_facultades, name='listar_facultades'),
    path('facultades/<int:facultad_id>/', views.detalle_facultad, name='detalle_facultad'),
    path('facultades/crear/', views.crear_facultad, name='crear_facultad'),
    path('facultades/editar/<int:facultad_id>/', views.editar_facultad, name='editar_facultad'),
    path('facultades/eliminar/<int:facultad_id>/', views.eliminar_facultad, name='eliminar_facultad'),
    path('facultades/<int:facultad_id>/departamentos-carreras/', views.departamentos_y_carreras_facultad, name='departamentos_y_carreras_facultad'),

    # Departamentos
    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('departamentos/<int:departamento_id>/', views.detalle_departamento, name='detalle_departamento'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
    path('departamentos/editar/<int:departamento_id>/', views.editar_departamento, name='editar_departamento'),
    path('departamentos/eliminar/<int:departamento_id>/', views.eliminar_departamento, name='eliminar_departamento'),
    path('departamentos/filtrar/', views.filtrar_departamentos, name='filtrar_departamentos'),
    path('departamentos/<int:departamento_id>/profesores/', views.profesores_por_departamento, name='profesores_por_departamento'),

    # Aulas
    path('aulas/', views.listar_aulas, name='listar_aulas'),
    path('aulas/<int:aula_id>/', views.detalle_aula, name='detalle_aula'),
    path('aulas/crear/', views.crear_aula, name='crear_aula'),
    path('aulas/editar/<int:aula_id>/', views.editar_aula, name='editar_aula'),
    path('aulas/eliminar/<int:aula_id>/', views.eliminar_aula, name='eliminar_aula'),
    path('aulas/filtrar/', views.filtrar_aulas, name='filtrar_aulas'),

    # Reportes y Estadísticas
    path('reportes/estudiantes/', views.reporte_estudiantes, name='reporte_estudiantes'),
    path('reportes/estudiantes-por-curso/', views.reporte_estudiantes_por_curso, name='reporte_estudiantes_por_curso'),
    path('reportes/cursos-por-profesor/', views.cursos_por_profesor, name='cursos_por_profesor'),
    path('reportes/inscripciones-por-semestre/', views.reporte_inscripciones_por_semestre, name='reporte_inscripciones_por_semestre'),
]
