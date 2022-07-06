from django.http import Http404
from django.shortcuts import render
from .models import Notes
# Create your views here.
def notes_list(request):
    return render(request, 'notes.json')

def note_detail(request):
    allNotes = Notes.objects.all()
    return render(request, 'note_details.html',{"notes":allNotes})

def private_notes(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except:
        raise Http404("Note not found")
    return render(request, 'private_notes.html',{"note":note})