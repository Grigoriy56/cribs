from django.urls import path
from . import views #импорт views из этой же директории

urlpatterns = [
    path('', views.index),  # при переходе на главную страницу будет показываться функция index из файла views
    path('about-us', views.about),
]
