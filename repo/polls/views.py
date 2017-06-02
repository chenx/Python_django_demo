# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice


def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = { 'latest_question_list': latest_question_list }
  return render(request, 'polls/index.html', context)

def index3(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list,
  }
  return HttpResponse(template.render(context, request))

def index2(request):
  output = "<p>Hello, world. You're at the polls index. <a href=\"../\">Home</a></p>"
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  output += ','.join([q.question_text for q in latest_question_list])
  return HttpResponse(output)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})

def detail2(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail2.html', {'question': question})
  # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  # response = "You're looking at the results of question %s."
  # return HttpResponse(response % question_id)
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  # return HttpResponse("You're voting on question %s." % question_id)
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice",
    })
  else:
    # selected_choice.votes += 1
    # https://docs.djangoproject.com/en/1.11/ref/models/expressions/#avoiding-race-conditions-using-f
    selected_choice.votes = F('votes') + 1  # avoid race condition
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
Code below are for generic view. But does not work.
 - template_name does not hide default.
 - result page does not show
"""
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_NAME = 'polls/results.html'

