from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response as Res
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from survey.serializers import SurveySerializer, QuestionSerializer, ResponseSerializer, ResponseSerializer
from survey.models import Survey, Question, BaseResponse, Response 
# Create your views here.

class ListSurvey(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class  DetailSurvey(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class ListQuestionSurvey(generics.ListCreateAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.filter(survey = self.kwargs['survey'])
        return queryset

    def get_serializer_context(self):
        data = {
            'request': self.request,
            'view': self,
            'format': self.request.GET.get('format') if self.request and self.request.GET else None,
            "survey_id": self.kwargs.get('survey'),
        }
        return data

class DetailQuestion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        queryset = Question.objects.filter(survey=self.kwargs["survey"])
        return queryset



class FillSurvey(APIView):
    serializer_class = ResponseSerializer

    def get(self,request,*args,**kwargs):
        survey = Survey.objects.get(pk=kwargs['survey'])
        question = Question.objects.get(pk=kwargs['question_pk'])
        return Res({'survey':survey.name,'question':question.question_text})

    def post(self,request, *args,**kwargs):
        data = request.data
        data._mutable=True
        data['question'] = Question.objects.get(pk=kwargs['question_pk']),
        data['survey'] = Survey.objects.get(pk=kwargs['survey']), 

        print(data)
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Res(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {'errors': 'You have already answered this question.'}
            return Res(data, status=status.HTTP_400_BAD_REQUEST)

   
   