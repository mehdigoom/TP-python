from rest_framework import serializers, fields
from . import models

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('question_text', 'pub_date',)