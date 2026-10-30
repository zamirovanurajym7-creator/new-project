class Movie:
    def __init__(self, title, director, year, genre, rating, duration):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating
        self.duration = duration
        
    def is_classic(self):
        return self.year < 2000
        
    def describe(self):
        return f"Фильм: '{self.title}' ({self.year}), Режиссёр: {self.director}, Жанр: {self.genre}, Рейтинг: {self.rating}"
        
    def duration_hours(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours} ч {minutes} мин"

# 3 объект түзүү
m1 = Movie("Титаник", "Джеймс Кэмерон", 1997, "драма", 7.9, 194)
m2 = Movie("Матрица", "Вачовски", 1999, "боевик", 8.7, 136)
m3 = Movie("Коко", "Ли Ункрич", 2017, "анимация", 8.4, 105)

for m in [m1, m2, m3]:
    print(m.describe())
    print(f"Классикабы (<2000): {m.is_classic()}")
    print(f"Узактыгы: {m.duration_hours()}\n")