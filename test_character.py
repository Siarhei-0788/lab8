import pytest
from abc import ABC, abstractmethod

# Определение интерфейсов
class ICharacterBuilder(ABC):
    @abstractmethod
    def set_class(self, character_class):
        pass

    @abstractmethod
    def set_weapon(self, weapon):
        pass

    @abstractmethod
    def set_armor(self, armor):
        pass

    @abstractmethod
    def add_skill(self, skill):
        pass

    @abstractmethod
    def build(self):
        pass

class ICharacterDirector(ABC):
    @abstractmethod
    def create_warrior(self):
        pass

    @abstractmethod
    def create_mage(self):
        pass

# Реализация классов
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

class CharacterBuilder(ICharacterBuilder):
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

class CharacterDirector(ICharacterDirector):
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

# Фикстуры для тестов
@pytest.fixture
def builder():
    return CharacterBuilder()

@pytest.fixture
def director(builder):
    return CharacterDirector(builder)

# Тесты для проверки интерфейсов
def test_builder_implements_interface(builder):
    assert isinstance(builder, ICharacterBuilder)

def test_director_implements_interface(director):
    assert isinstance(director, ICharacterDirector)

# Тесты для проверки создания персонажей
def test_create_warrior(director):
    character = director.create_warrior()
    assert character.character_class == "Воин"
    assert character.weapon == "Меч"
    assert character.armor == "Латные доспехи"
    assert "Сила" in character.skills
    assert "Защита" in character.skills

def test_create_mage(director):
    character = director.create_mage()
    assert character.character_class == "Маг"
    assert character.weapon == "Посох"
    assert character.armor == "Мантия"
    assert "Огненный шар" in character.skills
    assert "Ледяная стрела" in character.skills

# Тест для проверки строкового представления персонажа
def test_character_str():
    character = Character()
    character.character_class = "Воин"
    character.weapon = "Меч"
    character.armor = "Латные доспехи"
    character.skills = ["Сила", "Защита"]
    expected_output = (
        "Персонаж: Воин\n"
        "Оружие: Меч\n"
        "Броня: Латные доспехи\n"
        "Навыки: Сила, Защита"
    )
    assert str(character) == expected_output
    
    