# Create your views here.
from django.http import HttpResponse, Http404
from polls.models import Poll, Choice
from django.template import Context, loader
from django.shortcuts import render_to_response, render, get_object_or_404
from IPython.core.completer import get__all__entries

def index(request):
    latest_poll_list = Poll.objects.all()
    #===========================================================================
    # output = ', '.join([p.question for p in latest_poll_list])
    # t = loader.get_template('polls/index.html')
    # c = Context({
    #             'latest_poll_list':latest_poll_list,})
    # return HttpResponse(t.render(c))
    #===========================================================================
    return render(request,'polls/index.html',{'latest_poll_list':latest_poll_list})
def detail(request,poll_id):
    try:
        poll_obj = Poll.objects.get(pk=poll_id)
        print "examining the poll object - ", poll_obj.question
    except Poll.DoesNotExist:
        raise Http404
    return render(request,'polls/detail.html',{'poll':poll_obj})

def results(request,poll_id):
    poll_obj = get_object_or_404(Poll,pk=poll_id)
    selected_choice = poll_obj.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes = selected_choice.votes + 1
    selected_choice.save()
    message = '%s' % selected_choice
    return render(request,'polls/results.html',{'message':message,'poll':poll_obj})

def vote(request,poll_id):
    poll_obj = get_object_or_404(Poll,pk=poll_id)
    #choice_obj = get__all__entries(Choice,poll=poll_obj)   
    return render(request,'polls/vote.html',{'poll':poll_obj})