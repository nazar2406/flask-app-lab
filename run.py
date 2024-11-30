from app import create_app

app = create_app()  # Виклик функції створення додатка

if __name__ == '__main__':
    app.run(debug=True)  # Запуск додатка
