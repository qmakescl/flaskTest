from flask import Flask

# create_app은 플라스크 내부에서 정의된 함수명으로 애플리케이션 팩토링 방법
# 내부에 플라스크 애플리케이션을 생성하는 코드를 작성
def create_app():
    app = Flask(__name__)

    # @app.route : URL과 플라스크 코드를 매핑하는 데코레이터
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'
    # blueprint를 사용하면 라우트 함수를 모듈로 분리할 수 있음
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


