from django.urls import path, re_path
from survey import views
urlpatterns = [
    path('listsurvey',views.ListSurvey.as_view()),
    path('detailsurvey/<int:pk>/',views.DetailSurvey.as_view()),
    path('<int:survey>/listquestion/',views.ListQuestionSurvey.as_view()),
    path('<int:survey>/detailquestion/<int:pk>',views.DetailQuestion.as_view()),
    path('<int:survey>/questions/<int:question_pk>/fillSurvey/',views.FillSurvey.as_view()),
]