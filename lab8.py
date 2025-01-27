import curses

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

# Функция для отображения персонажа
def display_character(stdscr, character):
    stdscr.clear()
    stdscr.addstr("Созданный персонаж:\n", curses.color_pair(1))
    stdscr.addstr(str(character) + "\n\n", curses.color_pair(1))
    stdscr.addstr("Нажмите любую клавишу для продолжения...", curses.color_pair(1))
    stdscr.getch()

# Функция для отображения текстового интерфейса
def draw_menu(stdscr):
    curses.curs_set(0)  # Скрываем курсор
    stdscr.clear()
    stdscr.refresh()

    # Цвета
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    builder = CharacterBuilder()
    director = CharacterDirector(builder)

    current_row = 0
    menu_items = ["Создать Воина", "Создать Мага", "Выйти"]

    while True:
        stdscr.clear()
        stdscr.addstr("Добро пожаловать в генератор персонажей RPG!\n\n", curses.color_pair(1))

        for idx, item in enumerate(menu_items):
            if idx == current_row:
                stdscr.addstr(f"> {item}\n", curses.color_pair(2))
            else:
                stdscr.addstr(f"  {item}\n", curses.color_pair(1))

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
            if current_row == 0:
                character = director.create_warrior()
                display_character(stdscr, character)
            elif current_row == 1:
                character = director.create_mage()
                display_character(stdscr, character)
            elif current_row == 2:
                break

# Запуск программы
def main():
    curses.wrapper(draw_menu)
    print("Спасибо за использование генератора персонажей!")

if __name__ == "__main__":
    main()
    