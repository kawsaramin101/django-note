from django.contrib import admin

from .models import Note, NoteEditHistory

admin.site.register(Note)
admin.site.register(NoteEditHistory)
