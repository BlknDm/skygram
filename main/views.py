from flask import render_template, Blueprint, jsonify
from utils import get_posts_all
from db import db


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates", static_folder="static")


@main_blueprint.route('/test_db')
def test_db():
    result = db.session.execute(
        '''
        SELECT 1
        '''
    ).scalar()

    return jsonify(
        {
            'result': result
        }
    )


@main_blueprint.route('/')
def main_page():
    """ Представление основной страницы"""

    all_posts = get_posts_all()
    return render_template("index.html", all_posts=all_posts)


@main_blueprint.errorhandler(404)
def page_not_found(e):
    """ Представление страницы с ошибкой 404"""

    return render_template("404.html"), 404


@main_blueprint.errorhandler(500)
def internal_server_error(e):
    """ Представление страницы с ошибкой 505"""

    return render_template('500.html'), 500
