import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator

from .forms import NoteForm



def index(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            note_form = NoteForm(json.loads(request.body))

            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.creator = request.user
                note.save()
                context = {
                    "note": note
                }
                return render(request, 'notes/partials/note.html', context, status=201)
            context = {
                "note_form": note_form
            }
            return render(request, 'notes/partials/note-form.html', context, status=400)

        else:
            note_form = NoteForm()
            notes = request.user.notes.all()

            paginator = Paginator(notes, 100)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                "page_obj": page_obj,
                "note_form": note_form,
            }
            return render(request, "notes/index.html", context)
    else:
        return HttpResponse("Not Authenticated")



def note_details(request):
    pass