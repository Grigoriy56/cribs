from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('algem', views.algem, name = 'algem'),
    path('matrix', views.matrix, name = 'matrix'),
    path('matrix_a', views.matrix_a, name = 'addition'),
    path('matrix_mult', views.matrix_mult, name = 'mult'),
    path('matrix_milt1', views.matrix_mult1, name = 'mult1'),
    path('matrix_transpose', views.matrix_tr, name = 'tr'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
