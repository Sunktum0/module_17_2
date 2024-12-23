from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.bd import Base  # абсолютный импорт

class User(Base):
    __tablename__ = 'users'

    # Определите свои колонки здесь

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")