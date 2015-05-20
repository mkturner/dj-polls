from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from poll.models import Question

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World. You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." %
                        question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)
