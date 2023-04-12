import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking.settings')
django_asgi_app = get_asgi_application()

import random
from credit.models import *


def randomizer():
    return random.randint(10**15+1,10**16)


client1 = Client.objects.create(name='Бердиев Н.Д.', citizenship='Кыргызстан', birth_year=1994, work_place='Codify')
client2 = Client.objects.create(name='Ташмаматов А.О.', birth_year=1993, citizenship='Сомали')

account1 = Account.objects.create(number = randomizer(), account_type='2', client=client1)
account2 = Account.objects.create(number = randomizer(), client=client1)
account3 = Account.objects.create(number = randomizer(), account_type='3', client=client2)
account4 = Account.objects.create(number = randomizer(), client=client2)

credit1 = Credit.objects.create(sum=50_000, account=account1)
credit2 = Credit.objects.create(sum=15_000, account=account2)
credit3 = Credit.objects.create(sum=5_000, account=account3)
credit4 = Credit.objects.create(sum=100_000, account=account4)
