from django.contrib import admin

# Register your models here.
from core.models import Task, Worker, Replay, Match

admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(Replay)
admin.site.register(Match)