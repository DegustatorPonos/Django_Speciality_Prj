from django.shortcuts import render
import requests
import re
from .models import Paragraph

# Create your views here.

from django.http import HttpResponse

def index(request):
	content = Paragraph.objects.filter(targetpage='main')
	return render(request, 'main/ContentPage.html', {'title': 'Главная страница', 'content':content})

def relevance(request):
	content = Paragraph.objects.filter(targetpage='relevance')
	return render(request, 'main/ContentPage.html', {'title': 'Востребованность', 'content':content})

def geo(request):
	content = Paragraph.objects.filter(targetpage='geo')
	return render(request, 'main/ContentPage.html', {'title': 'География', 'content':content})


def skills(request):
	content = Paragraph.objects.filter(targetpage='skills')
	return render(request, 'main/ContentPage.html', {'title': 'Навыки', 'content':content})


def recent(request):
	url = 'https://api.hh.ru/vacancies?per_page=10&page=0&date_from=20240118&text=c%23&order_by=publication_time'
	data = requests.get(url, timeout=5).json()
	content = data['items']
	for i in content:
		info = requests.get(i['url'], timeout=5).json()
		i['desc'] = re.sub(r'<[^>]*>','',info['description'])[:250]+'...'
		i['skills'] = ', '.join([j['name'] for j in info['key_skills']])
	return render(request, 'main/VacancyPage.html', {'title': 'Последние вакансии', 'content':content})
