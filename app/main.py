from app.db import engine, Base
from app.user import User
from app.task import Task

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Вывод SQL-запросов
print("SQL для User:")
print(User.__table__)

print("\nSQL для Task:")
print(Task.__table__)