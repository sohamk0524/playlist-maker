from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		
		fields = ('name', 'genre', 'cover')
		model = Song