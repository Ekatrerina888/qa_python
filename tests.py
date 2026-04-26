import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_initial_state(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {} and collector.get_list_of_favorites_books() == []

    def test_add_new_book_correct_add_book_successful_add(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_book_genre('Азбука') == ''

    @pytest.mark.parametrize("name, expected_count", [
        ('Азбука', 1),
        ('', 0),
        ('Азбука' * 10, 0)
    ])
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест на добавление одной книги
    def test_add_new_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1
        assert 'Война и мир' in collector.get_books_genre()

    # Тест на невозможность добавления книги с пустым названием
    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # Тест на невозможность добавления книги с слишком длинным названием (>40 символов)
    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        long_name = 'а' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # Тест на установку жанра книге (параметризация)
    @pytest.mark.parametrize("book_name, genre", [
        ("Книга о фантастике", "Фантастика"),
        ("Страшный рассказ", "Ужасы"),
        ("Детективная история", "Детективы"),
        ("Мультфильм для детей", "Мультфильмы"),
        ("Комедийная повесть", "Комедии")
    ])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест на попытку установить неверный жанр
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Неверная книга')
        collector.set_book_genre('Неверная книга', 'Романтика')  # жанра нет в self.genre
        assert collector.get_book_genre('Неверная книга') == ''  # жанр не должен измениться

    # Тест на получение списка книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Звёздный путь')
        collector.set_book_genre('Звёздный путь', 'Фантастика')
        collector.add_new_book('Тайны прошлого')
        collector.set_book_genre('Тайны прошлого', 'Детективы')
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Звёздный путь' in fantasy_books
        assert len(fantasy_books) == 1

    # Тест на список книг для детей (без жанров из genre_age_rating)
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская сказка')
        collector.set_book_genre('Детская сказка', 'Мультфильмы')
        collector.add_new_book('Страшная история')
        collector.set_book_genre('Страшная история', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Детская сказка' in children_books
        assert 'Страшная история' not in children_books

    # Тест на добавление книги в «Избранное»
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # Тест на удаление книги из «Избранного»
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert 'Книга для удаления' not in collector.get_list_of_favorites_books()

    # Тест на попытку добавить в «Избранное» несуществующую книгу
    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    def test_set_book_genre_correct_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.books_genre['Азбука'] == 'Ужасы'

    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'FFFFFF')
        assert collector.books_genre['Азбука'] == ''

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    def test_get_books_with_specific_genre_duplicate(self):
        collector = BooksCollector()
        books = ['Азбука', 'Алгебра', 'Маленький принц']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')

        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_books_genre() == {'Азбука': ''}

    def test_get_books_for_children_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == ['Азбука']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        collector.delete_book_from_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_new_book('Алгебра')
        collector.add_book_in_favorites('Азбука')
        collector.add_book_in_favorites('Алгебра')
        assert collector.get_list_of_favorites_books() == ['Азбука', 'Алгебра']