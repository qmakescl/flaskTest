from flask import Blueprint

# 첫번째 인수 'main'으로 인해 main_views.py는 프로젝트 내에서 main이라는 이름으로 사용
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'