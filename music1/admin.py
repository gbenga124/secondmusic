from django.contrib import admin
from .models import Artiste
from .models import Song
from .models import Lyrics
# Register your models here.
admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)
