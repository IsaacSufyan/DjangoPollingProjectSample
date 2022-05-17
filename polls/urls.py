from django.urls import path
from . import views

# add namespaces to your App_Url for Differentiation during access in Templates (HTML)
app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('details/<int:question_id>/', views.index, name='detail'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('<int:question_id>/results/', views.result, name='results'),
# ]

# ------------------- Generic View ---------------------
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailViews.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]