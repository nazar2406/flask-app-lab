from flask import Flask

def create_app(config_name='config'):
    # Ініціалізація Flask-додатка
    app = Flask(__name__)

    # Завантаження конфігурації
    app.config.from_object(config_name)  # конфігурація з config.py

    # Реєстрація блюпринтів у контексті додатка
    with app.app_context():
        from . import views  # імпорт основних представлень
        from .posts import post_bp  # імпорт блупринта постів
        from .users import user_bp  # імпорт блупринта користувачів
        app.register_blueprint(post_bp)  # реєстрація блюпринта постів
        app.register_blueprint(user_bp)  # реєстрація блюпринта користувачів

    return app
