from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from django.template import RequestContext, loader

from .models import Question, Segment
# Create your views here.

question_count = Question.objects.count()

question_list = Question.objects.order_by('?')

#question_id = 0

correct_count = 0

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

def game(request):
    #global question_id
    try:
        count = request.POST['count']
    except (KeyError):
        correct_count = 0
        question_id = 0
        # Redisplay the question voting form.
        '''
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
        '''
    else:
        print count
        correct_count = int(count)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('agame:results', args=(p.id,)))
    
    question = question_list[question_id]
    segment_list = question.segment_set.order_by('?')
    question_id += 1
    is_last_question = (question_id == question_count)

    context = {'question' : question, 'question_id' : question_id, 'correct_count' : correct_count,
               'segment_list' : segment_list, 'is_last_question' : is_last_question}
    return render(request, 'agame/game.html', context)

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)
'''
def results(request):
    #global question_id
    #question_id = 0
    try:
        count = request.POST['count']
    except (KeyError):
        context = {'error_message' : "No result"}
        return render(request, 'agame/results.html', context);
    else:
        correct_count = int(count)
        context = {'correct_count' : correct_count}
        return render(request, 'agame/results.html', context)

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