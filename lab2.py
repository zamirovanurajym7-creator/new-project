class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным')
        self.__owner = owner
        self.__balance = balance
        self.__log = []  # список операций

    @property
    def owner(self):  # только чтение
        return self.__owner

    @property
    def balance(self):  # только чтение
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('Сумма пополнения должна быть положительной')
            return False
        self.__balance += amount
        self.__log.append(f'+{amount} сом (пополнение)')
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print('Сумма снятия должна быть положительной')
            return False
        if amount > self.__balance:
            print(f'Недостаточно средств. Доступно: {self.__balance} сом')
            return False
        self.__balance -= amount
        self.__log.append(f'-{amount} сом (снятие)')
        return True

    def get_statement(self):
        lines = [f'Выписка по счёту. Владелец: {self.__owner}', '-' * 40]
        for i, op in enumerate(self.__log, 1):
            lines.append(f'{i}. {op}')
        lines.append('-' * 40)
        lines.append(f'Текущий баланс: {self.__balance} сом')
        return '\n'.join(lines)


# Счёт 1: 5 операций
a1 = BankAccount('Актан', 5000)
a1.deposit(2000)
a1.withdraw(1500)
a1.deposit(500)
a1.withdraw(10000)  # отказ
a1.withdraw(800)
print(a1.get_statement())
print()

# Счёт 2: 5 операций
a2 = BankAccount('Айжан', 1000)
a2.deposit(3000)
a2.withdraw(500)
a2.deposit(-100)  # ошибка
a2.withdraw(2000)
a2.deposit(700)
print(a2.get_statement())




class StudentCard:
    def __init__(self, name, card_id, gpa):
        self.__name = name
        self.__card_id = card_id
        self.gpa = gpa  # идёт через сеттер, значит проверка сработает

    @property
    def name(self):
        return self.__name

    @property
    def card_id(self):
        return self.__card_id

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if not (0.0 <= value <= 4.0):
            raise ValueError('GPA должен быть в диапазоне 0.0-4.0')
        self.__gpa = value

    @property
    def status(self):  # вычисляемое свойство
        if self.__gpa >= 3.5:
            return 'Отличник'
        elif self.__gpa >= 2.5:
            return 'Хорошист'
        elif self.__gpa >= 1.0:
            return 'Удовлетворительно'
        return 'Отчислен'


students = [
    StudentCard('Айбек Асанов', 'S001', 3.9),
    StudentCard('Айжан Мирекова', 'S002', 3.6),
    StudentCard('Нурбек Исаев', 'S003', 2.8),
    StudentCard('Эмир Токтоев', 'S004', 1.5),
    StudentCard('Салтанат Жумабаева', 'S005', 0.7),
]

for s in students:
    print(f'{s.card_id} | {s.name:<15} | GPA {s.gpa:<4} | {s.status}')

avg = sum(s.gpa for s in students) / len(students)
excellent = sum(1 for s in students if s.status == 'Отличник')
print(f'\nСредний GPA: {avg:.2f}')
print(f'Количество отличников: {excellent}')

# Проверка валидации
try:
    students[0].gpa = 5.0
except ValueError as e:
    print('Ошибка:', e)
    
    
    
class MedCard:
    BLOOD_GROUPS = {'I+', 'I-', 'II+', 'II-', 'III+', 'III-', 'IV+', 'IV-'}

    def __init__(self, patient, age, blood_group):
        if blood_group not in self.BLOOD_GROUPS:
            raise ValueError(f'Группа крови должна быть одной из: {sorted(self.BLOOD_GROUPS)}')
        self.__patient = patient
        self.age = age  # через сеттер
        self.__blood_group = blood_group
        self.__diagnoses = []

    @property
    def patient(self):
        return self.__patient

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 150):
            raise ValueError('Возраст должен быть от 0 до 150')
        self.__age = value

    @property
    def is_adult(self):
        return self.__age >= 18

    def add_diagnosis(self, text):
        if text in self.__diagnoses:
            print(f'Диагноз «{text}» уже есть')
            return False
        self.__diagnoses.append(text)
        return True

    def remove_diagnosis(self, text):
        if text not in self.__diagnoses:
            print(f'Диагноза «{text}» нет в карте')
            return False
        self.__diagnoses.remove(text)
        return True

    def summary(self):
        diag = ', '.join(self.__diagnoses) if self.__diagnoses else 'нет'
        return (f'Пациент: {self.__patient}\n'
                f'Возраст: {self.__age} ({"взрослый" if self.is_adult else "ребёнок"})\n'
                f'Группа крови: {self.__blood_group}\n'
                f'Диагнозы: {diag}\n' + '-' * 30)


c1 = MedCard('Айдар Асанов', 25, 'II+')
c2 = MedCard('Айжан Бекова', 12, 'I-')
c3 = MedCard('Бакыт Уулу', 67, 'IV+')

c1.add_diagnosis('Гастрит')
c1.add_diagnosis('Мигрень')
c2.add_diagnosis('Аллергия на пыльцу')
c3.add_diagnosis('Гипертония')
c3.add_diagnosis('Диабет 2 типа')
c3.remove_diagnosis('Диабет 2 типа')
c3.remove_diagnosis('Астма')  # нет такого диагноза

for c in (c1, c2, c3):
    print(c.summary())

try:
    c1.age = 200
except ValueError as e:
    print('Ошибка:', e)
    
    
    
    
class EWallet:
    def __init__(self, owner, balance, currency, max_transfer):
        if balance < 0 or max_transfer <= 0:
            raise ValueError('Баланс >= 0 и лимит перевода > 0')
        self.__owner = owner
        self.__balance = balance
        self.__currency = currency
        self.__max_transfer = max_transfer

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):  # только чтение
        return self.__balance

    @property
    def can_transfer(self):  # можно ли вообще переводить
        return self.__balance > 0

    def deposit(self, amount):
        if amount <= 0:
            print('Сумма должна быть положительной')
            return False
        self.__balance += amount
        return True

    def transfer(self, recipient, amount):
        if not isinstance(recipient, EWallet):
            print('Получатель должен быть кошельком EWallet')
            return False
        if recipient is self:
            print('Нельзя переводить самому себе')
            return False
        if recipient.__currency != self.__currency:  # доступ к приватному полю другого объекта того же класса
            print('Валюты кошельков не совпадают')
            return False
        if amount <= 0:
            print('Сумма перевода должна быть положительной')
            return False
        if amount > self.__max_transfer:
            print(f'Превышен лимит перевода ({self.__max_transfer} {self.__currency})')
            return False
        if amount > self.__balance:
            print(f'Недостаточно средств. Баланс: {self.__balance} {self.__currency}')
            return False
        
        self.__balance -= amount
        recipient.__balance += amount
        print(f'{self.__owner} → {recipient.__owner}: {amount} {self.__currency}')
        return True

    def __str__(self):
        return f'{self.__owner}: {self.__balance} {self.__currency}'


w1 = EWallet('Айдар', 10000, 'KGS', 5000)
w2 = EWallet('Айжан', 2000, 'KGS', 3000)
w3 = EWallet('Нурбек', 500, 'KGS', 1000)

w1.transfer(w2, 3000)  # OK
w2.transfer(w3, 4000)  # превышен лимит (3000)
w2.transfer(w3, 2500)  # OK
w3.transfer(w1, 5000)  # превышен лимит
w3.transfer(w1, 2900)  # OK? лимит 1000 -> превышен
w3.transfer(w1, 1000)  # OK
w1.transfer('Бек', 100)  # не кошелёк
print()

print(f'{w1} | can_transfer = {w1.can_transfer}')
print(f'{w2} | can_transfer = {w2.can_transfer}')
print(f'{w3} | can_transfer = {w3.can_transfer}')




class SecurePassword:
    def __init__(self, pwd=None):
        self.__password = None
        if pwd is not None:
            self.password = pwd

    @staticmethod
    def __errors(pwd):
        """Возвращает список нарушенных условий."""
        errs = []
        if len(pwd) < 8:
            errs.append('Длина должна быть не менее 8 символов')
        if not any(ch.isdigit() for ch in pwd):
            errs.append('Нужна хотя бы одна цифра')
        if not any(ch.isupper() for ch in pwd):
            errs.append('Нужна хотя бы одна заглавная буква')
        if ' ' in pwd:
            errs.append('Пароль не должен содержать пробелов')
        return errs

    @property
    def password(self):
        # реальный пароль наружу не отдаём
        return '*' * len(self.__password) if self.__password else None

    @password.setter
    def password(self, pwd):
        errs = self.__errors(pwd)
        if errs:
            for e in errs:
                print(' X ', e)
            return  # пароль не меняется
        self.__password = pwd
        print(' ✓ Пароль установлен')

    def check(self, pwd):
        return self.__password == pwd

    def strength(self, pwd=None):
        """Сила по числу выполненных условий (из 4)."""
        if pwd is None:
            pwd = self.__password or ''
        done = 4 - len(self.__errors(pwd))
        if done == 4:
            return 'Сильный'
        elif done == 3:
            return 'Средний'
        return 'Слабый'


sp = SecurePassword()
tests = ['abc', 'abcdefgh', 'Abcdefgh', 'Abcdefg1', 'Strong Pass1']
for p in tests:
    print(f'Пароль: "{p}" → сила: {sp.strength(p)}')
    sp.password = p
    print()

sp.password = 'MyPass2026'
print('check верный : ', sp.check('MyPass2026'))
print('check неверный:', sp.check('qwerty'))
print('Показ пароля : ', sp.password)




class TariffPlan:
    def __init__(self, name, price, speed, minutes, sms):
        self.__name = name
        self.price = price  # через сеттер
        self.__speed = speed
        self.__minutes = minutes
        self.__sms = sms

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Цена должна быть > 0')
        self.__price = value

    @property
    def speed(self):
        return self.__speed

    @property
    def minutes(self):
        return self.__minutes

    @property
    def sms(self):
        return self.__sms

    @property
    def value_score(self):
        """Условная «выгодность»: чем больше услуг на 1 сом, тем лучше."""
        return (self.__speed * 2 + self.__minutes * 0.1 + self.__sms * 0.2) / self.__price

    def annual_cost(self):
        return self.__price * 12

    def discount_price(self, percent):
        if not (0 <= percent <= 100):
            raise ValueError('Скидка должна быть от 0 до 100%')
        return round(self.__price * (1 - percent / 100), 2)

    def compare(self, other):
        rows = [
            ('Цена, сом/мес', self.price, other.price),
            ('Скорость, Мбит/с', self.speed, other.speed),
            ('Минуты', self.minutes, other.minutes),
            ('SMS', self.sms, other.sms),
        ]
        print(f'{"":<18}{self.name:<12}{other.name:<12}')
        for label, a, b in rows:
            print(f'{label:<18}{a:<12}{b:<12}')
        cheaper = self if self.price < other.price else other
        print(f'Дешевле: {cheaper.name}')


plans = [
    TariffPlan('Эконом', 300, 20, 300, 50),
    TariffPlan('Стандарт', 550, 50, 800, 200),
    TariffPlan('Премиум', 900, 150, 2000, 500),
    TariffPlan('Безлимит', 1200, 300, 5000, 1000),
]

for p in plans:
    print(f'{p.name:<10} год: {p.annual_cost():>6} сом | со скидкой 15%: {p.discount_price(15):>7} | score = {p.value_score:.3f}')
print()

plans[0].compare(plans[1])
best = max(plans, key=lambda p: p.value_score)
print(f'\nОптимальный тариф: {best.name} (score {best.value_score:.3f})')

try:
    plans[0].price = 0
except ValueError as e:
    print('Ошибка:', e)
    
    
    
    
class Safe:
    MAX_ATTEMPTS = 3

    def __init__(self, pin, master_pin):
        self.__pin = str(pin)
        self.__master_pin = str(master_pin)
        self.__content = []
        self.__attempts = 0
        self.__locked = False

    @property
    def is_locked(self):
        return self.__locked

    def __verify(self, pin):
        """Проверка PIN со счётчиком попыток (приватный метод)."""
        if self.__locked:
            print('Сейф заблокирован. Нужен мастер-PIN.')
            return False
        if str(pin) == self.__pin:
            self.__attempts = 0
            return True
        self.__attempts += 1
        left = self.MAX_ATTEMPTS - self.__attempts
        if left <= 0:
            self.__locked = True
            print('Неверный PIN. Сейф заблокирован!')
        else:
            print(f'Неверный PIN. Осталось попыток: {left}')
        return False

    def open(self, pin):
        if self.__verify(pin):
            print('Открыто. Содержимое:', self.__content or 'пусто')
            return True
        return False

    def put(self, item, pin):
        if self.__verify(pin):
            self.__content.append(item)
            print(f'Положено: {item}')
            return True
        return False

    def reset(self, master_pin):
        if str(master_pin) == self.__master_pin:
            self.__locked = False
            self.__attempts = 0
            print('Сейф разблокирован.')
            return True
        print('Неверный мастер-PIN.')
        return False


s = Safe('1234', '9999')
s.put('Паспорт', '1234')
s.put('Деньги', '1234')
s.open('1234')
print('--- перебор ---')
s.open('0000')
s.open('1111')
s.open('2222')  # блокировка
s.open('1234')  # даже верный PIN не работает
s.reset('0000')  # неверный мастер-PIN
s.reset('9999')
s.open('1234')




class HealthMetrics:
    def __init__(self, name, height, weight, age, sex):
        self.__name = name
        self.height = height  # через сеттеры
        self.weight = weight
        self.age = age
        if sex not in ('м', 'ж'):
            raise ValueError('Пол: "м" или "ж"')
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        if not (50 <= v <= 250):
            raise ValueError('Рост должен быть 50-250 см')
        self.__height = v

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, v):
        if not (2 <= v <= 500):
            raise ValueError('Вес должен быть 2-500 кг')
        self.__weight = v

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        if not (0 <= v <= 150):
            raise ValueError('Возраст должен быть 0-150')
        self.__age = v

    def bmi(self):
        h = self.__height / 100  # см -> м
        return round(self.__weight / h ** 2, 1)

    def bmi_status(self):
        b = self.bmi()
        if b < 18.5:
            return 'Недовес'
        elif b < 25:
            return 'Норма'
        elif b < 30:
            return 'Избыточный вес'
        elif b < 40:
            return 'Ожирение'
        return 'Морбидное ожирение'

    def daily_calories(self, activity=1.2):
        """Формула Харриса–Бенедикта (пересмотренная, 1984) + коэффициент активности."""
        w, h, a = self.__weight, self.__height, self.__age
        if self.__sex == 'м':
            bmr = 88.362 + 13.397 * w + 4.799 * h - 5.677 * a
        else:
            bmr = 447.593 + 9.247 * w + 3.098 * h - 4.330 * a
        return round(bmr * activity)


patients = [
    HealthMetrics('Айдар', 178, 55, 20, 'м'),
    HealthMetrics('Айжан', 165, 58, 19, 'ж'),
    HealthMetrics('Нурбай', 175, 85, 35, 'м'),
    HealthMetrics('Салтанат', 160, 110, 45, 'ж'),
]

for p in patients:
    print(f'{p.name:<10} ИМТ: {p.bmi():<5} {p.bmi_status():<16} Калории: {p.daily_calories()} ккал/сут')

try:
    patients[0].height = 400
except ValueError as e:
    print('Ошибка:', e)
    