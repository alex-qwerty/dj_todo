import random

from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
    
        response = list()
        
        list_todo = (
            'Установить python',
            'Установить django',
            'Запустить сервер',
            'Порадоваться результату',
            'Добавить список дел',
            'Сделать произвольный выбор дел',
            'Отправить домашнее задание на проверку',
        )
        
        for item in random.sample(list_todo, 5):
            response.append(f'<li>{item}</li>')
            
        full_response = f'<ul> {"".join(response)}</ul>'
        
        return HttpResponse(full_response)
