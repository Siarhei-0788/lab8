import tkinter as tk
from tkinter import font

# Класс Character, который мы будем создавать
class Character:
    def __init__(self):
        self.character_class = None
        self.weapon = None
        self.armor = None
        self.skills = []

    def __str__(self):
        skills_str = ", ".join(self.skills) if self.skills else "нет навыков"
        return (f"Персонаж: {self.character_class}\n"
                f"Оружие: {self.weapon}\n"
                f"Броня: {self.armor}\n"
                f"Навыки: {skills_str}")

# Интерфейс Builder
class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_class(self, character_class):
        self.character.character_class = character_class
        return self

    def set_weapon(self, weapon):
        self.character.weapon = weapon
        return self

    def set_armor(self, armor):
        self.character.armor = armor
        return self

    def add_skill(self, skill):
        self.character.skills.append(skill)
        return self

    def build(self):
        return self.character

# Класс Director, который управляет процессом создания
class CharacterDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_warrior(self):
        return self.builder.set_class("Воин") \
                           .set_weapon("Меч") \
                           .set_armor("Латные доспехи") \
                           .add_skill("Сила") \
                           .add_skill("Защита") \
                           .build()

    def create_mage(self):
        return self.builder.set_class("Маг") \
                           .set_weapon("Посох") \
                           .set_armor("Мантия") \
                           .add_skill("Огненный шар") \
                           .add_skill("Ледяная стрела") \
                           .build()

# Функция для отображения информации о персонаже
def display_character(character):
    output_text.config(state=tk.NORMAL)  # Разрешаем редактирование
    output_text.delete(1.0, tk.END)  # Очищаем текстовое поле
    output_text.insert(tk.END, str(character))  # Вставляем текст
    output_text.config(state=tk.DISABLED)  # Запрещаем редактирование

# Функции для создания персонажей
def create_warrior():
    character = director.create_warrior()
    display_character(character)

def create_mage():
    character = director.create_mage()
    display_character(character)

# Инициализация строителя и директора
builder = CharacterBuilder()
director = CharacterDirector(builder)

# Создание графического интерфейса
root = tk.Tk()
root.title("Генератор персонажей RPG")
root.geometry("500x400")  # Устанавливаем размер окна

# Настройка шрифтов
title_font = font.Font(family="Helvetica", size=16, weight="bold")
button_font = font.Font(family="Helvetica", size=12)
text_font = font.Font(family="Courier", size=12)

# Заголовок
label = tk.Label(root, text="Выберите тип персонажа:", font=title_font)
label.pack(pady=10)

# Кнопки для создания персонажей
warrior_button = tk.Button(root, text="Создать Воина", command=create_warrior, font=button_font)
warrior_button.pack(pady=5)

mage_button = tk.Button(root, text="Создать Мага", command=create_mage, font=button_font)
mage_button.pack(pady=5)

# Текстовое поле для отображения информации о персонаже
output_text = tk.Text(root, height=10, width=50, font=text_font)
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)  # Запрещаем редактирование

# Кнопка выхода
quit_button = tk.Button(root, text="Выйти", command=root.quit, font=button_font)
quit_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()