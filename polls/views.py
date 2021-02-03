from django.template import loader
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'ultimas_questoes': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    template = loader.get_template('polls/details.html')
    context = {
        'question': get_object_or_404(Question, pk=question_id),
    }
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)