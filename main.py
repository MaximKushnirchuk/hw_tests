
import requests

# functions

def sort_uniq_names(mentors_list: list) :
    '''функция принимает на вход список из списков, в которых перечисляются данные людей (фамилии и имена), отделяет имена от фамилий и собирает все имена в один список. Имена уникальны (не повторяются) и отсортированы в алфавитном порядке'''
    set_names = set()
    for onest in mentors_list :
        for name in onest :
            name = name.split()
            set_names.add(name[0])
    unique_names = list(set_names)
    result = sorted(unique_names)
    return result


def top_three_popular_name(mentors_list: list):
    '''Функция определяет топ-3 популярных имён среди преподавателей'''
    all_list = []
    [all_list.extend(x) for x in mentors_list]
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    all_names_set = set(all_names_list)
    popular = [[all_names_list.count(x), x] for x in all_names_set]
    popular.sort(key=lambda x:x[0], reverse=True)
    result = [f"{str(x[1])}: {str(x[0])} раз(а)" for x in popular[:3]]
    return result


def longest_shortest_courses(mentors: list, courses: list, durations: list) :
    '''Код создаст кортеж из двух списков, в которых содержится : в первом - название самого короткого курса, во втором - название самого длинного курсов'''
    
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    max_dur = max(durations)
    min_dur = min(durations)
    maxes = []
    minis = []
    for id, duration in enumerate(durations):
        if duration == max_dur:
            maxes.append(id)
        elif duration == min_dur:
            minis.append(id)

    courses_max = [x["title"] for id, x in enumerate(courses_list) if id in maxes]
    courses_min = [x["title"] for id, x in enumerate(courses_list) if id in minis]

    return courses_min, courses_max 

def add_folder_yandex_disk(token: str, folder_name: str) :
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path' : folder_name}
    headers = {'Authorization' : token}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code

def check_folder_yandex_disk(token: str, folder_name: str) :
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path' : folder_name}
    headers = {'Authorization' : token}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code
