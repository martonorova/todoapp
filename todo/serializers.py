from rest_framework import serializers
from todo.models import Note
from django.utils import timezone

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =('id', 'note_title', 'note_text', 'date_created', 'is_done', 'user', 'deadline')

    def validate_deadline(self, value):
        if timezone.now() >= value:
            raise serializers.ValidationError(
            'Please return a valid deadline'
            )
        return value
