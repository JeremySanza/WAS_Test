from django.urls import path
from rango import views
app_name = 'school_news'

urlpatterns = [
    path('', views.index, name='index'),
]
