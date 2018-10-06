from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from api.views import ReplaysResource, AssignResource, GetReplayResource

replays_resources = ReplaysResource()
assign_resources = AssignResource()
get_replay_resources = GetReplayResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(replays_resources.urls)),
    url(r'^api/', include(assign_resources.urls)),
    url(r'^api/', include(get_replay_resources.urls)),
]