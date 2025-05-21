import random

from faker import Faker

faker = Faker()


def generate_registration_name():
    name = faker.name()
    return name


def generate_registration_email():
    email = f"dmitriy_romashov_23_{random.randint(100, 999)}@yandex.ru"
    return email


def generate_registration_password(len=12):
    password = faker.password(length=len, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password
