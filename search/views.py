import logging
from flask import Blueprint, render_template, request
from utils import search_for_posts, get_posts_by_user, get_posts_all


search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates", static_folder="static")


@search_blueprint.route('/search/', methods=['GET'])
def search_page():
    """ Представление  страницы поиска"""

    path = get_posts_all()
    recieved_word = request.args.get('s')
    posts = search_for_posts(path, recieved_word)
    if posts:
        return render_template("search.html", recieved_word=recieved_word, posts=posts)
    else:
        return "Информация не найдена"


@search_blueprint.route('/user/<name>', methods=['GET'])
def get_posts_user(name):
    """ Представление  страницы по конкретному пользователю"""

    try:
        post_data = get_posts_all()
        posts = get_posts_by_user(post_data, name)
        return render_template("user-feed.html", posts=posts)
    except ValueError:
        "Нет такого пользователя"


@search_blueprint.errorhandler(404)
def page_not_found(e):
    """ Представление страницы с ошибкой 404"""

    return render_template("404.html"), 404


@search_blueprint.errorhandler(500)
def internal_server_error(e):
    """ Представление страницы с ошибкой 505"""

    return render_template('500.html'), 500
