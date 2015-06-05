from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from django.template import RequestContext, loader

from .models import Question, Segment
# Create your views here.

total_count = Question.objects.count()

question_list = Question.objects.order_by('?')

'''class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
'''

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    formula = r'\sum_{1}^{n}{n^2}=\texttt{what}'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'formula' : formula,}
    return render(request, 'polls/index.html', context)

def game(request, question_id):
    question_id = int(question_id)
    question = question_list[question_id]
    segment_list = question.segment_set.order_by('?')
    is_last_question = (question_id + 1 == total_count)
    context = {'question' : question, 'segment_list' : segment_list,
               'is_last_quesiton' : is_last_question}
    return render(request, 'agame/game.html', context)

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_Segment = p.Segment_set.get(pk=request.POST['Segment'])
    except (KeyError, Segment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a Segment.",
        })
    else:
        selected_Segment.votes += 1
        selected_Segment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))