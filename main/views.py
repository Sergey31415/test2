from urllib import request

from django.db.models import Sum, Count
from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Answer


# Create your views here.
def home(request):
    answers = Answer.objects.all()

    # Фильтруем ответы по преподу и рассчитываем сумму и количество
    overall_stat = answers.filter(prepod=1)
    total_sum = overall_stat.aggregate(Sum('answer'))['answer__sum'] or 0
    total_count = overall_stat.aggregate(Count('answer'))['answer__count'] or 1

    # Рассчитываем среднее значение
    result = total_sum / total_count + 1

    return render(request, 'main.html', {'answers': answers, 'overall_stat': result})