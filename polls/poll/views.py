from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from poll.models import Choice, Question

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return last five published items'''
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Reload page with errors
        return render(request, 'poll/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
