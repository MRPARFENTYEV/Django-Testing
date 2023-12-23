import pytest
from rest_framework.test import APIClient
from  model_bakery import baker
from students.models import Course, Student

'''запуск - cd django_testing
 pytest'''
# def test_example():
#     assert False, "Just test example"

'''Тестовый тест(намеренная тавтология)'''
# @pytest.mark.django_db
# def test_api():
#
#     #Arrange
#     client = APIClient()
#     Course.objects.create(id=1, name = 'Django')
#
#     # Act
#     response = client.get('/courses/')
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 1
#     assert data[0]['name'] == 'Django'

'''Фикстура для api-client'''
@pytest.fixture()
def client():
    return APIClient()

''' Фикстура для создания студента( для выполнения задания не нужна)'''
# @pytest.fixture()
# def student():
#     # return Student.objects.create(id=1,name='Джанго',birth=18.04.1990) # Создание в ручную
#     return Student.objects.create(id=1Student.id, name=Student.name, birth=Student.birth_date)# Создание по христиански




'''Фикстура для фабрики курсов'''

@pytest.fixture()
def course_factory(*args,**kwargs):
    def factory():
        return baker.make(Course,*args, **kwargs)
    return factory

'''Фикстура для фабрики студентов'''

@pytest.fixture()
def course_factory(*args,**kwargs):
    def factory():
        return baker.make(Course,*args, **kwargs)
    return factory


'''проверка получения 1го курса (retrieve-логика)
    создаем курс через фабрику
    строим урл и делаем запрос через тестовый клиент
    проверяем, что вернулся именно тот курс, который запрашивали
'''


'''проверка получения списка курсов (list-логика)
    аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
'''


'''проверка фильтрации списка курсов по id
    создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
'''

'''проверка фильтрации списка курсов по name'''


'''тест успешного создания курса
    здесь фабрика не нужна, готовим JSON-данные и создаем курс
'''

'''тест успешного обновления курса
    сначала через фабрику создаем, потом обновляем JSON-данными
'''

'''тест успешного удаления курса'''

