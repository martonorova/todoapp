from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from . import serializers
from . import models

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is a todo app.")

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
