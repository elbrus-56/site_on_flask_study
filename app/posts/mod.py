from flask import Blueprint, request, render_template
from flask_paginate import Pagination, get_page_parameter

mod = Blueprint('users', __name__)

@mod.route('/')
def index():
    search = False
    # если в URL присутствует параметр поиска 'q'
    q = request.args.get('q')
    if q:
        search = True

    # определяем текущую страницу 
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # поиск пользователей
    users = User.find(...)
    pagination = Pagination(page=page, total=users.count(), search=search, record_name='users')
    # `page` это номер текущей страницы, параметр URL (по умолчанию 'page') из которого
    #  он будет извлекаться. Можно настроить, например Pagination(page_parameter='p', ...)
    # или установить `PAGE_PARAMETER` в файле конфигурации.
    # Также можно настроить параметр URL, который будет передавать количество выводимых  
    # записей на одной странице, например Pagination(per_page_parameter='pp') или установить 
    # параметр `PER_PAGE` в файле конфигурации

    return render_template('posts/index.html',
                           users=users,
                           pagination=pagination,
                           )