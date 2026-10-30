class Book:
    category ='Печатное издание'

    def __init__(self , title,author, year, pages):
        self.title =title
        self.author = author
        self.year =year
        self.pages = pages

    def age(self):
        return 2026-self.year

    def describe(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}, Страниц: {self.pages}'

    def is_long_read(self):
        return self.pages > 400


book1 =Book('Война и мир', 'Лев Толстой', 1869, 1225)
book2 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 96)
book3 =Book('Гарри Поттер', 'Джоан Роулинг', 1997, 500)

for book in [book1, book2, book3]:
    print(book.describe())
    print('Возраст книги:', book.age())
    print('Долгое чтение:', book.is_long_read())
    print()
    
    
    
class Pet:
    category='Домашнее животное'

    def __init__(self,name, species,age, weight):
        self.name = name
        self.species =species
        self.age = age
        self.weight =weight

    def describe(self):
        return f'Кличка: {self.name},Вид: {self.species}, Возраст: {self.age}, Вес: {self.weight} кг'

    def is_adult(self):
        return self.age>= 2

    def sound(self):
        sounds= {
            'кошка':'Мяу!',
            'собака': 'Гав!',
            'попугай': 'Кррр!',
            'черепаха':'Молчит'
        }
        return sounds.get(self.species,'Молчит')


pet1= Pet('Мурка','кошка', 3, 4)
pet2 = Pet('Бобик', 'собака', 2, 10)
pet3 =Pet('Кеша', 'попугай', 1, 0.5)
pet4= Pet('Тортилла', 'черепаха', 5, 2)

for pet in [pet1,pet2, pet3,pet4]:
    print(pet.describe())
    print('Взрослый:', pet.is_adult())
    print('Звук:', pet.sound())
    print()
    
    
class Recipe:
    def __init__(self, dish_name,cuisine, cook_time,difficulty, servings):
        self.dish_name = dish_name
        self.cuisine =cuisine
        self.cook_time = cook_time
        self.difficulty= difficulty
        self.servings =servings

    def is_quick(self, limit):
        return self.cook_time< limit

    def describe(self):
        return f'Блюдо:{self.dish_name}, Кухня:{self.cuisine}, Время приготовления: {self.cook_time} мин, Сложность: {self.difficulty}, Порций: {self.servings}'

    def per_person_time(self):
        return self.cook_time /self.servings


recipe1 =Recipe('Пицца', 'итальянская', 40, 'средний', 4)
recipe2= Recipe('Суши', 'японская', 60, 'сложный', 3)
recipe3=Recipe('Бешбармак','кыргызская', 120, 'сложный', 6)
recipe4 = Recipe('Тако', 'мексиканская', 25, 'лёгкий', 2)

for recipe in [recipe1,recipe2,recipe3, recipe4]:
    print(recipe.describe())
    print('Быстрое приготовление:',recipe.is_quick(30))
    print('Время на одну порцию:', recipe.per_person_time(), 'мин')
    print()
    
    
    
class Movie:
    def __init__(self, title,director, year,genre, rating, duration):
        self.title = title
        self.director =director
        self.year = year
        self.genre =genre
        self.rating = rating
        self.duration=duration

    def is_classic(self):
        return self.year <2000

    def describe(self):
        return f'Название:{self.title},Режиссёр:{self.director}, Год: {self.year}, Жанр: {self.genre}, Рейтинг: {self.rating}, Длительность: {self.duration} мин'

    def duration_hours(self):
        hours = self.duration// 60
        minutes = self.duration %60
        return f'{hours} ч {minutes} мин'


movie1=Movie('Титаник', 'Джеймс Кэмерон', 1997, 'драма', 9.0, 195)
movie2 =Movie('Маска', 'Чак Рассел', 1994, 'комедия', 8.5, 101)
movie3= Movie('Мстители', 'Джосс Уидон', 2012, 'боевик', 8.0, 143)

for movie in [movie1,movie2,movie3]:
    print(movie.describe())
    print('Классика:', movie.is_classic())
    print('Длительность:',movie.duration_hours())
    print()
    
    
    
class Planet:
    body_type ='Небесное тело'

    def __init__(self,name, diameter_km,mass_earth, moons, has_atmosphere):
        self.name = name
        self.diameter_km =diameter_km
        self.mass_earth = mass_earth
        self.moons =moons
        self.has_atmosphere =has_atmosphere

    def describe(self):
        return f'Название: {self.name},Диаметр: {self.diameter_km} км, Масса относительно Земли: {self.mass_earth}, Спутников: {self.moons}, Атмосфера: {self.has_atmosphere}'

    def gravity(self, earth_g=9.8):
        return earth_g *self.mass_earth

    def is_giant(self):
        return self.diameter_km >50000


planet1= Planet('Земля', 12742,1.0, 1, True)
planet2 =Planet('Юпитер', 139820, 317.8, 95, True)
planet3=Planet('Марс', 6779, 0.107, 2, True)

for planet in [planet1,planet2, planet3]:
    print(planet.describe())
    print('Гравитация:',planet.gravity())
    print('Планета-гигант:', planet.is_giant())
    print()
    
    
    
class Student:
    institution ='КГТУ им.И.Раззакова'

    def __init__(self, full_name,group, year,gpa):
        self.full_name= full_name
        self.group = group
        self.year =year
        self.gpa=gpa

    def introduce(self):
        return f'ФИО:{self.full_name}, Группа:{self.group},Курс: {self.year}, Средний балл: {self.gpa}'

    def academic_status(self):
        if self.gpa>=3.5:
            return 'Отличник'
        elif self.gpa >=2.5:
            return 'Хорошист'
        elif self.gpa >= 1.5:
            return 'Удовлетворительно'
        else:
            return 'Задолженность'

    def scholarship(self,base=3000):
        status = self.academic_status()

        if status =='Отличник':
            return base * 1.5
        elif status =='Хорошист':
            return base
        else:
            return 0


student1 =Student('Иванов Иван', 'ИТ-1-23',3, 3.8)
student2= Student('Петров Пётр','ИТ-2-23', 2, 3.0)
student3 =Student('Сидоров Алексей', 'ИИ-1-23',1, 2.0)

for student in [student1,student2, student3]:
    print(student.introduce())
    print('Учебный статус:',student.academic_status())
    print('Стипендия:',student.scholarship(), 'сом')
    print()
    
    
    
class Smartphone:
    def __init__(self,brand, model, ram_gb,battery_mah,year, price):
        self.brand =brand
        self.model = model
        self.ram_gb=ram_gb
        self.battery_mah= battery_mah
        self.year= year
        self.price =price

    def describe(self):
        return f'Бренд:{self.brand}, Модель:{self.model}, ОЗУ: {self.ram_gb} ГБ, Аккумулятор: {self.battery_mah} мАч, Год: {self.year}, Цена: {self.price} сом'

    def is_flagship(self, min_ram=8):
        return self.ram_gb >=min_ram

    def battery_days(self, usage_mah_per_day):
        return self.battery_mah /usage_mah_per_day


phone1 =Smartphone('Apple','iPhone 15', 8, 3349, 2023, 75000)
phone2 =Smartphone('Samsung', 'Galaxy S24', 8, 4000, 2024, 65000)
phone3= Smartphone('Xiaomi', 'Redmi Note 13', 6, 5000, 2024, 18000)
phone4 =Smartphone('Google', 'Pixel 9', 12, 4700, 2024, 70000)

for phone in [phone1,phone2, phone3, phone4]:
    print(phone.describe())
    print('Флагман:', phone.is_flagship())
    print('Дней без зарядки:',phone.battery_days(1000))
    print()
    
    
class WeatherStation:
    def __init__(self,name, city, altitude_m,temperature, humidity, wind_speed):
        self.name =name
        self.city= city
        self.altitude_m =altitude_m
        self.temperature =temperature
        self.humidity = humidity
        self.wind_speed =wind_speed

    def describe(self):
        return f'Название:{self.name}, Город: {self.city}, Высота: {self.altitude_m} м, Температура: {self.temperature} °C, Влажность: {self.humidity} %, Скорость ветра: {self.wind_speed} м/с'

    def feels_like(self):
        return round(self.temperature - self.wind_speed * 0.7)

    def weather_status(self):
        if self.temperature> 30:
            return 'Жарко'
        elif self.temperature > 15:
            return 'Тепло'
        elif self.temperature > 5:
            return 'Прохладно'
        else:
            return 'Холодно'

    def is_comfortable(self):
        return 40 <= self.humidity <= 70 and 18 <= self.temperature <= 26


station1 =WeatherStation('Метеостанция Бишкек', 'Бишкек', 800, 25, 55, 3)
station2= WeatherStation('Метеостанция Ош', 'Ош', 963, 32, 45, 2)
station3 = WeatherStation('Метеостанция Нарын', 'Нарын', 2044, 4, 75, 5)

for station in [station1, station2, station3]:
    print(station.describe())
    print('Ощущаемая температура:',station.feels_like(), '°C')
    print('Статус погоды:', station.weather_status())
    print('Комфортная погода:', station.is_comfortable())
    print()
    
    