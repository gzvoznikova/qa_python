Запустить проект можно с помощью команды в терминале: pytest tests.py -v
Сценарии, покрытые тестами:

test_add_new_book_add_two_books: проверка добавления двух книг
test_add_new_book_already_added_book: негативная проверка, проверка повторного добавления книги
test_add_new_book_invalid_length: проверка количества символов в названии книги 
test_set_book_genre_correct_genre: проверка на добавление жанра для книги 
test_set_book_genre_invalid_book: негативная проверка, проверка установки жанра несуществующей книге
test_set_book_genre_invalid_genre: негативная проверка, проверка установки несуществующего жанра
test_get_book_genre_list: проверка возврата словаря с жанрами 
test_get_books_for_children: проверка, что возвращаются только доступные детям книги
test_add_book_in_favorites: проверка добавления книги в избранное
test_add_book_in_favorites_not_exist: проверка, что нельзя добавить несуществующую книгу в избранное
test_delete_book_from_favorites: проверка на удаление книги из избранного
test_get_list_of_favorites_books_list: проверка на получение списка избранных книг