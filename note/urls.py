from django.urls import path
from .import views

urlpatterns = [
    path('', views.notes_list, name='notes'),
    path('details', views.note_detail, name='note_detail'),
    path('specific/<int:pk>', views.private_notes, name='private_notes'),
]
