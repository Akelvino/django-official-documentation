# from django.http import Http404
from django.shortcuts import render, get_object_or_404
# from django.template import loader
# from django.http import HttpResponse
from.models import Question

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list":latest_question_list,
#     }
    # return HttpResponse(template.render(context, request))
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(f"{output}")
    
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context= {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
    
#     return render(request, "polls/details.html", {"questiom":question})
    # return HttpResponse(f'you are looking at a question {question_id}')
    
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html",{"question": question})
   

def results(request, question_id):
    pass
    # return HttpResponse(f"You are looking at the results of question {question_id}")

def vote(request, question_id):
    pass
    # return HttpResponse(f"You are voting on question {question_id}")