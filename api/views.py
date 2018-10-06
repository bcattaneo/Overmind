from django.shortcuts import render
from django.http import HttpResponse
import base64
from tastypie.resources import ModelResource, Resource
from api.models import Replays, Assign
from tastypie.authorization import Authorization
from django.conf import settings
from tastypie import fields
import json

# Folder where to store replay files
REPLAYS_DIR = settings.REPLAYS_DIR

class ReplaysResource(ModelResource):
    class Meta:
        queryset = Replays.objects.all()
        resource_name = 'replays'
        authorization = Authorization()
        fields = ['title', 'base64_file', 'date'] # Limiting fields

    # obj_create override, in order to do something when on POST
    def obj_create(self,bundle,**kwargs):
        bundle = super(ReplaysResource,self).obj_create(bundle,**kwargs)

        # Save recieved base64 encoded file
        request_base64_file = bundle.data['base64_file']
        request_title = bundle.data['title']
        fullpath = REPLAYS_DIR + request_title
        replay_file = open(fullpath, "wb")
        replay_file.write(base64.b64decode(request_base64_file))
        replay_file.close()

        return bundle

class AssignResource(ModelResource):
    replay = fields.ForeignKey(ReplaysResource, 'replay', full=True)

    class Meta:
        queryset = Assign.objects.all()
        resource_name = 'assign'
        authorization = Authorization()
        fields = ['replay', 'overlord', 'date', 'update'] # Limiting fields

# Return next available (or timed-out) replay to process
class GetReplayResource(Resource):
    class Meta:
        allowed_methods = None
        list_allowed_methods = ['get']
        resource_name = 'get_replay'

    # get_list override, in order to do something when on GET
    def get_list(self, request, **kwargs):
        # OBTENER ACA overlord que viene en GET
        replay = Replays.objects.get(title='prueba7.SC2Replay')
        data = {'title': replay.title, 'base64_file': replay.base64_file}
        # Busco primer replay sin asignacion,
        # si encuentro, creo registro en Assign para el overlord que me lo pidio
        # si no encuentro, busco en los Assign alguno que este timeout, y actualizo Overlord y fecha update
        # si no encuentro nada, retorno 404 en vez de 200
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json', status=200)