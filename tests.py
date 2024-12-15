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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '', 'Что делать, если ваш кот хочет вас убить': ''}

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_already_added_book(self): # Проверка повторного добавления книги
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    def test_add_new_book_invalid_length_max_limit(self):  # Проверка ограничения на 40  символов
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомбиГордость и предубеждение и зомби')
        assert collector.get_books_genre() == {}

    def test_add_new_book_invalid_length_min_limit(self):# Проверка ограничения на  0 символов
        collector = BooksCollector()
        collector.add_new_book('')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_correct_genre(self):# Проверка установки жанра  книге
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_set_book_genre_invalid_book(self):# Проверка установки жанра несуществующей книге
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_invalid_genre(self):# Проверка установки несуществующего жанра
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Неизвестный жанр')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    def test_get_book_genre_list(self):# Проверка возврата всего словаря
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_for_children(self): #проверяет, что возвращаются только доступные детям книги
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites(self): #проверяет добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_not_exist(self): #проверяет, что нельзя добавить несуществующую книгу в избранное
        collector = BooksCollector()
        book = 'Гордость и предубеждение'
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self): #проверяет возможность удаления книги из избранного
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_list(self):  #проверяет вывод книг из избранного
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']
