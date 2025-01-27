import pytest
from lab8.py import Character, CharacterBuilder, CharacterDirector

# Замените your_script_name на имя файла, в котором находится ваш код

# Фикстура для создания директора
@pytest.fixture
def director():
    builder = CharacterBuilder()
    return CharacterDirector(builder)

# Тест для создания воина
def test_create_warrior(director):
    warrior = director.create_warrior()
    
    assert warrior.character_class == "Воин"
    assert warrior.weapon == "Меч"
    assert warrior.armor == "Латные доспехи"
    assert "Сила" in warrior.skills
    assert "Защита" in warrior.skills
    assert len(warrior.skills) == 2

# Тест для создания мага
def test_create_mage(director):
    mage = director.create_mage()
    
    assert mage.character_class == "Маг"
    assert mage.weapon == "Посох"
    assert mage.armor == "Мантия"
    assert "Огненный шар" in mage.skills
    assert "Ледяная стрела" in mage.skills
    assert len(mage.skills) == 2