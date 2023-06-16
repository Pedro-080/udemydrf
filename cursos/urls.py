from django.urls import path
from .views import CursoAPIView,AvaliacaoAPIView

urlpatterns = [
    path('cursos/',CursoAPIView.as_view(),name='cursos')
]
