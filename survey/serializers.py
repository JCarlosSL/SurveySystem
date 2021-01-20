from rest_framework import serializers
from survey.models import Survey, Question, Response, BaseResponse

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text',)

    def validate(self, data):
        if not data.get('survey_id'):
            data['survey_id'] = self.context.get('survey_id')
        if data.get('id') == 0:
            del data['id']
        return data

class BaseResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseResponse
        exclude = ['response']


class ResponseSerializer(serializers.ModelSerializer):
    survey = serializers.SlugRelatedField(
        read_only=True,
        slug_field=Survey
    )
    question = serializers.SlugRelatedField(
        read_only=True,
        slug_field=Question
    )
    class Meta:
        model = Response
        fields = '__all__'
        #exclude = ['survey','question']

    def create(self, validated_data):
        print(validated_data)
        response = Response.objects.create(**validated_data)
        #response.survey = self.survey
        #response.question = self.question
        return response.save()
    """def save(self,commit=False):
        response = super(ResponseSerializer,self).save()
        response.survey = self.survey
        response.question = self.question
        response.save()

        return response"""   
    
