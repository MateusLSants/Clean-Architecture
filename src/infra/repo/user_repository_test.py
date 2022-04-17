from faker import Faker
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()


def insert_user():
    """Should insert user"""

    name = faker.name()
    password = faker.word()

    user_repository.insert_user(name, password)
