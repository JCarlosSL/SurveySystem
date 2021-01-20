from django.test import TestCase

from survey.models import (Question, 
                            Response,
                            BaseResponse,
                            Survey)
from survey.serializers import SurveySerializer

class TestSurvey(TestCase):
    def setUp(self):
        self.Sv = Survey()
        self.Sv.name = "Plantas"
        self.Sv.description = "ya jale todo"
        self.Sv.save()

        self.Qs = Question()
        self.Qs.question_text = "¿es GG?"
        self.Qs.survey = self.Sv

        self.Rs = Response()
        self.name = "Carlos"
        self.survey = self.Sv

        self.BRs = BaseResponse()
        self.BRs.response = self.Rs
        self.BRs.question = self.Qs
        self.BRs.response_text = "Al año con fuerza"
    
    def testdatabase(self):
        all_database=Survey.objects.all()
        assert len(all_database) == 1
        
        only_database=all_database[0]

        assert only_database == self.Sv

