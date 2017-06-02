from django.conf.urls import url

from . import views

app_name ='polls'
urlpatterns = [
  # ex: /polls/
  ## url(r'^$', views.index, name='index'),
  # ex: /polls/index3
  ## url(r'^index3/$', views.index3, name='index3'),
  # ex: /polls/index2
  ## url(r'^index2/$', views.index2, name='index2'),
  # ex: /polls/5/
  ## url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
  # ex: /polls/5/detail
  url(r'^(?P<question_id>[0-9]+)/detail/$', views.detail2, name='detail2'),
  # ex: /polls/5/results/
  ## url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
  # ex: /polls/5/vote/
  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

  # generic views
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]
