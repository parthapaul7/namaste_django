from django.contrib import admin
from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Notes, NotesAdmin)