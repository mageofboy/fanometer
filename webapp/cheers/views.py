from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context = {'table': [["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"]],
                'chicken': ["meow"]}
    return render(request, 'cheers/index.html', context)

def main(request):
    context = {'bands': ["1","2","3","4","5","6","7","8","5654","6","5478","647","545r","436","547","5476","54","754","yrf","hf","hre","tre","tre","yre","ytr","y64","754","543","7657","535","2","5437","56u","y","r","htru","t4y","436","246","426","42"]}
    return render(request, 'cheers/main.html', context)
