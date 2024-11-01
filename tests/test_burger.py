import praktikum.ingredient_types
from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database

class TestBurger:

    """Тест на установку булочек."""
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Name_bun', 120.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    """Тест на добавление ингредиента."""
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_ingredient'
        mock_ingredient.get_price.return_value = 50.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 50.0
        assert burger.ingredients[0].get_name() == 'Name_ingredient'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE

    """Тест на удаление ингредиента."""
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    """Тест на перемещение ингредиента."""
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    """Тест на получение цены бургера."""
    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])  # Убедитесь, что индексы правильные
        assert burger.get_price() == 500.0  # Обновите ожидаемую цену

    """Тест на получение чека."""
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])  # Убедитесь, что индексы правильные
        expected_receipt = "(==== black bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= sauce sour cream =\n"\
                           "(==== black bun ====)\n\n"\
                           "Price: 500"
        assert expected_receipt == burger.get_receipt()

    """Тест на удаление ингредиента с некорректным индексом."""
    def test_remove_ingredient_out_of_bounds(self):
        burger = Burger()
        if len(burger.ingredients) > 0:
            burger.remove_ingredient(0)  # Попытка удаления ингредиента с индексом 0, когда список пуст
        assert len(burger.ingredients) == 0
