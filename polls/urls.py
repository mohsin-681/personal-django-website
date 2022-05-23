from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/index.html', views.IndexView.as_view(), name='index'),
    path('about.html/index.html', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about.html/', views.AboutView.as_view(), name='about'),
    path('contact.html/', views.ContactView.as_view(), name='contact'),
]
