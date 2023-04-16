from faker import Faker
from demoqa.data.data import Person


faker_ru = Faker('ru_RU')
Faker.seed()

def get_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )




# from faker.providers import internet
#
# fake = Faker()
# fake.add_provider(internet)
# faker_ru = Faker('ru_RU')
#
#
# print(fake.name())
# print(fake.address())
# print(faker_ru.name())
# print(faker_ru.address())
# print(fake.text())
# print(faker_ru.text())
# print(fake.ipv4_private())